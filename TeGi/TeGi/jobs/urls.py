from django.urls import path
from .views import home, landing_page, gig_jobs, tech_jobs, login_view, register_view, post_job_view, profile_view, login_as_seeker
from django.contrib.auth.views import LogoutView
from .views import poster_profile, delete_job, edit_job, login_as_poster
urlpatterns = [
    # Landing page and main job views
    path('', landing_page, name='landing_page'),  # Set landing page as the root URL
    path('home/', home, name='home'),
    path('gig-jobs/', gig_jobs, name='gig_jobs'),
    path('tech-jobs/', tech_jobs, name='tech_jobs'),

    # Authentication
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='landing_page'), name='logout'),

    # User Profile and Post Jobs
    path('profile/', profile_view, name='profile'),
    path('post-job/', post_job_view, name='post_job'),
    
    # Job Poster Routes
    path('poster-profile/', poster_profile, name='poster_profile'),
    path('delete-job/<int:job_id>/', delete_job, name='delete_job'),
    path('edit-job/<int:job_id>/', edit_job, name='edit_job'),

      # Uncomment if needed for login as specific role (e.g., Seeker or Poster)
    path('login-as-seeker/', login_as_seeker, name='login_as_seeker'),
    path('login-as-poster/', login_as_poster, name='login_as_poster'),

]