# users/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')  # Updated related_name
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    skills = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField(default=0)
    experience = models.TextField()
    talents = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.user.username