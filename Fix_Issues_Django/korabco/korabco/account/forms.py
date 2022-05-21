# Django imports
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from account.models import Profile

User = get_user_model()


class UserLoginForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(attrs={
            "name": "email", "class": "input100",
            "placeholder": "Email"
        }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "name": "password",  "class": "input100",
            "placeholder": "Password"
        }))


class UserRegisterForm(UserCreationForm):
    """
        Creates User registration form for signing up.
    """

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(max_length=254, required=True, widget=
                             forms.EmailInput(attrs={
                                 "name": "email", "class": "input100",
                                 "placeholder": "Email"
                                                    }
                                              ),
                             help_text='Required. Input a valid email address.'
                             )

    first_name = forms.CharField(max_length=30, required=True, widget=
                             forms.TextInput(attrs={
                                 "name": "name", "class": "input100",
                                 "placeholder": "Name"
                                                    }
                                              ),
                             help_text='Required. Input a name.'
                             )

    password1 = forms.CharField(widget=
                                forms.PasswordInput(attrs={
                                 "name": "password1", "class": "input100",
                                 "placeholder": "Password"
                                                    }
                                                    ), validators=[]
                                )

    password2 = forms.CharField(widget=
                                forms.PasswordInput(attrs={
                                 "name": "password2", "class": "input100",
                                 "placeholder": "Confirm Password"
                                                    }

                                                    ), validators=[]
                                )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'password1', 'password2']
        widgets = {

            "email": forms.EmailInput(attrs={
                "name": "email", "class": "input100",
                "placeholder": "Email"
            }),


        }


class UserUpdateForm(forms.ModelForm):
    """
        Creates form for user to update their account.
    """
    email = forms.EmailField(widget=
                             forms.EmailInput(attrs={
                                                     'name': "email",
                                                     'id': "email",
                                                     'class': "form-control"
                                                    }
                                              ),
                             )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {

            'first_name': forms.TextInput(attrs={
                'name': "first-name",
                'class': "form-control",
                'id': "first-name",
                'required': "required"
            }),

            'last_name': forms.TextInput(attrs={
                'name': "last-name",
                'class': "form-control",
                'id': "last-name",
                'required': "required"
            }),

        }


class ProfileUpdateForm(forms.ModelForm):
    """
       Creates form for user to update their Profile.
    """
    class Meta:
        model = Profile
        fields = ['avatar', 'address', 'city', 'country', 'zip_code']

        widgets = {

            'avatar': forms.FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "profileImage"
            }),

            'address': forms.TextInput(attrs={
                'name': "address",
                'class': "form-control",
                'id': "address",
                'required': "required"
            }),

            'city': forms.TextInput(attrs={
                'name': "city",
                'class': "form-control",
                'id': "city",
                'required': "required"
            }),

            'country': forms.TextInput(attrs={
                'name': "country",
                'class': "form-control",
                'id': "country",
                'required': "required"
            }),

            'zip_code': forms.TextInput(attrs={
                'name': "zip-code",
                'class': "form-control",
                'id': "zip-code",
                'required': "required"
            }),

        }
