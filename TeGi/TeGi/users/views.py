# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile

def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            # Create UserProfile
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': user_form})

def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=user_profile)
    return render(request, 'users/profile.html', {'form': profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if role == 'poster' and user.is_job_poster:  # Assuming you have a way to check if user is a job poster
                return redirect('poster_profile')  # Redirect to job poster dashboard
            elif role == 'seeker' and user.is_job_seeker:
                return redirect('seeker_dashboard')  # Redirect to job seeker dashboard
        
    
    return render(request, 'login.html')