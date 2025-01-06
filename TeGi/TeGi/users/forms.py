# users/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email','password']

class UserProfileForm(forms.ModelForm):
    # New field for photo upload
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = [
            'profile_photo',  # Added photo upload field
            'skills',
            'description',
            'email',
            'phone_number',
            'age',
            'experience',
            'talents',
            'resume'
        ]