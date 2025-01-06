from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50, choices=[
        ('Freelancer', 'Freelancer'),
        ('Part Time', 'Part Time'),
        ('Full Time', 'Full Time'),
        ('Work From Home', 'Work From Home'),
        ('Onfield', 'Onfield'),
    ])
    location = models.CharField(max_length=100)
    timing = models.CharField(max_length=50)
    pay_range = models.CharField(max_length=50)
    description = models.TextField()
    experience_required = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_gig = models.BooleanField(default=False)  # True for gig jobs, False for tech jobs

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile')  # Updated related_name
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