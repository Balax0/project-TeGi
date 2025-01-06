from django import forms
from .models import Job, UserProfile
from django.contrib.auth.models import User

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'job_type', 'location', 'timing', 'pay_range', 'description', 'experience_required', 'is_gig']

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

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']