from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout, get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from .models import Job
from .forms import CustomUserCreationForm, LoginForm
from .forms import JobForm
from django.shortcuts import render, get_object_or_404, redirect
# Import the User model
User = get_user_model()
# Create your views here.
def home_view(request):
    jobs = Job.objects.all()
    return render(request,"main/home.html",{'jobs':jobs})

def about(request):
    return render(request,"main/about.html",{})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')  # Redirect to the login page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'main/register.html', {'form': form})

# for login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email)
            print(password)
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')  # Redirect to your homepage URL name
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"Error in {field}: {error}")
                        messages.error(request, "Registration failed. Please correct the errors.")
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})

def job_list(request):
    # Fetch all jobs or apply filters based on a search query
    query = request.GET.get('q')
    if query:
        jobs = Job.objects.filter(name__icontains=query)
    else:
        jobs = Job.objects.all()

    # Pass the job data to the template
    context = {
        'jobs': jobs,
    }
    return render(request, 'main/job_list.html', context)

# for creating jobs
def job_create_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job created successfully!')
            return redirect('/')  # Redirect to a list or detail view after saving
    else:
        form = JobForm()
    
    return render(request, 'main/job_form.html', {'form': form})

# for updating jobs
def job_update_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('/')  # Redirect to a list or detail view after saving
    else:
        form = JobForm(instance=job)
    
    return render(request, 'main/job_update.html', {'form': form, 'job': job})

# for delete
def job_confirm_delete_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('/')  # Redirect to a list or detail view after deleting
    
    return render(request, 'main/job_confirm_delete.html', {'job': job})

