# Core Django imports.
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from account.views import (
    UserLoginView,
    UserLogoutView,
    ActivateView,
    AccountActivationSentView,
    UserRegisterView,
    ProfileUpdatedView,
)

app_name = "account"

urlpatterns = [
    # Account
    path(route='login/', view=UserLoginView.as_view(), name='login'),
    path(route='register/', view=UserRegisterView.as_view(), name='register'),
    path(route='logout/', view=UserLogoutView.as_view(), name='logout'),
    path(route='activation_sent/', view=AccountActivationSentView.as_view(), name='activation_sent'),
    path(route='activate/<uidb64>/<token>/', view=ActivateView.as_view(), name='activate'),
    path(route='profile/update/', view=ProfileUpdatedView.as_view(), name='profile_update'),

    # Password Reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html',
                                              subject_template_name='mails/password_reset_subject.txt',
                                              email_template_name='mails/password_reset_email.html',
                                              html_email_template_name='mails/password_reset_email.html',
                                              success_url=reverse_lazy('account:password_reset_done')),
                                              name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',
                                                     success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
]
