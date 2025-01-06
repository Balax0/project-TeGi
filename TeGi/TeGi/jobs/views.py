from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import JobForm, UserProfileForm, UserRegistrationForm
from .models import Job, UserProfile
from django.contrib.auth.decorators import login_required
# jobs/views.py

def home(request):
    return render(request, 'jobs/home.html')

def gig_jobs(request):
    jobs = Job.objects.filter(is_gig=True)
    return render(request, 'jobs/gig_jobs.html', {'jobs': jobs})

def tech_jobs(request):
    jobs = Job.objects.filter(is_gig=False)
    return render(request, 'jobs/tech_jobs.html', {'jobs': jobs})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')


# def login_view(request):
#     if request.method == 'POST':
#         login_type = request.POST.get('login_type')
#         if login_type == 'seeker':
#             return redirect('home')  # Redirect to seeker's home page
#         elif login_type == 'poster':
#             return redirect('poster_profile')  # Redirect to poster's profile page
#     return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def post_job_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'jobs/profile.html', {'profile': user_profile})


# jobs/views.py
def landing_page(request):
    return render(request, 'jobs/landing.html')


@login_required
def poster_profile(request):
    jobs = Job.objects.filter(user=request.user)  # Get jobs posted by the logged-in user
    return render(request, 'jobs/poster_profile.html', {'jobs': jobs})

@login_required
def delete_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('poster_profile')  # Redirect to the poster profile page

@login_required
def edit_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('poster_profile')  # Redirect to the poster profile page
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/post_job.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')  # Redirect based on user type
    return render(request, 'login.html')


@login_required
def login_as_seeker(request):
    # Implement login as seeker logic here
    return redirect('home')  # Redirect to seeker's home page

@login_required
def login_as_poster(request):
    # Implement login as poster logic here
    return redirect('poster_profile')  # Redirect to poster's profile


