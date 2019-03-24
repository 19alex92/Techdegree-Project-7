import re

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django_password_strength.widgets import (PasswordStrengthInput,
                                              PasswordConfirmationInput)
from django.utils.safestring import mark_safe

from bootstrap_datepicker_plus import DatePickerInput
from froala_editor.widgets import FroalaEditor


from .models import Profile


class UserRegisterForm(UserCreationForm):
    '''Form which adds the Email field to the sign up process'''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PasswordStrengthForm(PasswordChangeForm):
    '''Tried to add a password strength meter but it is not working'''
    new_password1 = forms.CharField(
        widget=PasswordStrengthInput()
    )
    new_password2 = forms.CharField(
        widget=PasswordConfirmationInput(confirm_with='new_password1')
    )

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(PasswordStrengthForm, self).__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = mark_safe(
            '<ul>\n'
            '<li>Must not be the same as the current password</li>\n'
            '<li>Minimum password length of 14 characters</li>\n'
            '<li>Must use both uppercase and lowercase letters</li>\n'
            '<li>Must include one or more numerical digits</li>\n'
            '<li>The password must contain one or more of the following'
            ' symbols: ()[]{}|\\~!@#$%`^&"*_-+=;:,<>./?</li>\n'
            '<li>Cannot contain your username or parts of your full name,'
            ' such as your first name</li>\n'
            '</ul>'
        )


class ChangeEmailForm(forms.ModelForm):
    '''Form to change and validate the email'''
    email = forms.EmailField(label="Current Email")
    email1 = forms.EmailField(label="New Email")
    email2 = forms.EmailField(label="New Email Confirmation")

    class Meta:
        model = User
        fields = ['email', 'email1', 'email2']

    def clean(self):
        email = self.cleaned_data['email']
        email1 = self.cleaned_data['email1']
        email2 = self.cleaned_data['email2']
        if email == email1 or email == email2:
            raise forms.ValidationError("New Email can't be"
                                        " the same as the old")
        elif email1 != email2:
            raise forms.ValidationError("Emails must match")
        return self.cleaned_data

    def save(self):
        user = super(ChangeEmailForm, self).save(commit=False)
        user.email = self.cleaned_data['email1']
        user.save()
        return user


class UserEditForm(forms.ModelForm):
    '''Lets the user edit the username'''
    class Meta:
        model = User
        fields = ['username']


class ProfileEditForm(forms.ModelForm):
    '''Lets the user edit it's profile data'''
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'favorite_animal',
            'favorite_food',
            'hobby',
            'bio',
            'image',
        ]
        widgets = {
            'date_of_birth': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'extraFormats': ['MM/DD/YY', 'MM/DD/YYYY', ],
                }
            ),
            'bio': FroalaEditor()
        }
        input_formats = {
            'date_of_birth': ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
        }

    def clean_bio(self):
        bio = self.cleaned_data['bio']
        clean_text = re.sub("<.*?>", "", bio)
        if len(clean_text) < 10:
            raise forms.ValidationError("Provide at least 10 characters"
                                        " or more in your bio")
        return bio
