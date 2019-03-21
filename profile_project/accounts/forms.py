from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

from bootstrap_datepicker_plus import DatePickerInput
from froala_editor.widgets import FroalaEditor

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class ChangeEmailForm(forms.ModelForm):
    email = forms.EmailField()
    email1 = forms.EmailField(label="New Email")
    email2 = forms.EmailField(label="New Email Confirmation")

    class Meta:
        model = User
        fields = ['email','email1', 'email2']
    
    def clean(self):
        email = self.cleaned_data['email']
        email1 = self.cleaned_data['email1']
        email2 = self.cleaned_data['email2']
        if email == email1 or email == email2:
            raise forms.ValidationError("New Email can't be the same as the old")
        elif email1 != email2:
            raise forms.ValidationError("Emails must match")
        return self.cleaned_data


class ProfileEditForm(forms.ModelForm):
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
            'date_of_birth': DatePickerInput(),
            'bio': FroalaEditor()
        }

    def clean_bio(self):
        bio = self.cleaned_data['bio']
        if len(bio) <= 10:
            raise forms.ValidationError("Provide at least 10 characters or more in your bio")
        return bio