from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Job

# Import the User model
User = get_user_model()
# Create your views here.
def home(request):
    jobs = Job.objects.all()
    return render(request,"main/home.html",{'jobs':jobs})

def about(request):
    return render(request,"main/about.html",{})

def register_view(request):
    #  User = get_user_model()
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'main/register.html')

# for quick serach
# views.py
 # Assuming your model is named Job

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


    # if request.method == 'POST':
    #     username = request.POST.['username']
    #     email = request.POST.['email']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']

    #     if password1 != password2:
    #         messages.error(request, "Passwords do not match.")
    #     elif User.objects.filter(username=username).exists():
    #         messages.error(request, "Username already exists.")
    #     elif User.objects.filter(email=email).exists():
    #         messages.error(request, "Email is already in use.")
    #     else:
    #         user = User.objects.create_user(username=username, email=email, password=password1)
    #         user.save()
    #         messages.success(request, "Registration successful. Please log in.")
    #         return redirect('home')
       
        

    # return render(request, 'main/register.html')

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Django's authenticate method uses username, so retrieve the user by email
#         user = User.objects.filter(email=email).first()
#         if user:
#             user = authenticate(request, username=user.username, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Login successful!")
#             return redirect('home')  # Redirect to your home view
#         else:
#             messages.error(request, "Invalid email or password.")

#     return render(request, 'main/login.html')

# #@login_required
# def logout_view(request):
#     logout(request)
#     messages.info(request, "Logged out successfully.")
#     return redirect('login')

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Authenticate user
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
#             # Login user
#             login(request, user)
#             return redirect('home')  # Redirect to a home page or dashboard
#         else:
#             messages.error(request, 'Invalid email or password')

#     return render(request, 'login.html')  # Make sure the template name matches your file

