# Django imports.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View

from account.models import Profile
from account.forms import UserLoginForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from account.token import account_activation_token
from korabco import settings


User = get_user_model()


class UserLoginView(View):
    """
     Logs user into dashboard.
    """
    template_name = 'account/login.html'
    context_object = {"login_form": UserLoginForm}

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        login_form = UserLoginForm(data=request.POST)

        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                return redirect('dashboard:home')

            else:
                messages.error(request, "Invalid email or password !")
                return render(request, self.template_name, self.context_object)

        else:
            messages.error(request, "Invalid email or password !")
            return render(request, self.template_name, self.context_object)


class UserRegisterView(View):
    """
      View to let users register
    """
    template_name = 'account/register.html'
    context_object = {"register_form": UserRegisterForm()}

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super(UserRegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        register_form = UserRegisterForm(request.POST or None)

        email = request.POST.get('email')
        is_username_exists = User.objects.filter(username=email).exists()

        if register_form.is_valid() and not is_username_exists:
            user = register_form.save(commit=False)
            user.is_active = False
            user.save()

            # Create profile
            profile = Profile()
            profile.user = user
            profile.save()

            current_site = get_current_site(request)
            subject = 'Activate your Korabco account'
            context_mail = {
                'user': user,
                'domain': current_site.domain,
                'protocol': request.scheme,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            }
            html_content = render_to_string('mails/account_activation_email.html', context_mail)
            text_content = render_to_string('mails/account_activation_email.txt', context_mail)
            user.email_user(subject=subject, message=text_content, html_message=html_content)
            return redirect('account:activation_sent')

        else:
            msg_error = "Something went wrong ! please try again or contact us it the error persist."
            if is_username_exists:
                msg_error = f"This email is already used ! please choose another email or click " \
                            f"reset password if you don't remember it."
            if not register_form.is_valid():
                msg_error = register_form.errors
            messages.error(request, msg_error)
            return render(request, self.template_name, {"register_form": register_form})


class AccountActivationSentView(View):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super(AccountActivationSentView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'account/account_activation_sent.html')


class ActivateView(View):
    """
     Activate user accounts.
    """

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super(ActivateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user,token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()

            login(request, user)
            msg = 'Congratulations! Your account was activated successfully.'
            messages.success(request, msg)
            return redirect('account:login')
        else:
            return render(request, 'account/account_activation_invalid.html')


class UserLogoutView(View):
    """
     Logs user out of the dashboard.
    """

    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not connected yet to process logout.')
        else:
            logout(request)
            messages.success(request, 'You have successfully logged out.')

        return redirect(reverse('account:login'))


class ProfileUpdatedView(LoginRequiredMixin, View):
    """
     Updates account profile details
    """
    template_name = 'account/profile_update.html'
    context_object = {}

    def get(self, request):
        user_form = UserUpdateForm(instance=self.request.user)
        profile_form = ProfileUpdateForm(instance=self.request.user.profile)

        self.context_object['user_form'] = user_form
        self.context_object['profile_form'] = profile_form

        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(data=request.POST, instance=self.request.user)
        profile_form = ProfileUpdateForm(data=request.POST, files=request.FILES,
                                         instance=self.request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            messages.success(request, 'Your account has successfully been updated!')
            return redirect('account:profile_update')

        else:
            user_form = UserUpdateForm(instance=self.request.user)
            profile_form = ProfileUpdateForm(instance=self.request.user.profile)

            self.context_object['user_form'] = user_form
            self.context_object['profile_form'] = profile_form

            messages.error(request, f'Invalid data. Please provide valid data.')
            return render(request, self.template_name, self.context_object)
