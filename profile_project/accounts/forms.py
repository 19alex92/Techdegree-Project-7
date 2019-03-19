from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


#class PasswordEditForm(forms.ModelForm):
 #   class Meta:
  #      model = User
   #     fields = ['password1', 'password2']

# Von django PasswordChangeForm selber schreiben und inherit from SetPasswordForm mit feldern new_password1, new_password2, old_password


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
            'image'
        ]