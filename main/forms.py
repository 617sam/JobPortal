from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms
from .models import Job

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "role", "password1", "password2")
        widgets = {
            'role': forms.HiddenInput()  # Optionally hide the role field during registration
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "role")

        
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'details', 'address', 'salary', 'location', 'level', 'openings']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 4}),
            'salary': forms.NumberInput(attrs={'step': '0.01'}),
            'level': forms.Select(choices=Job.LEVEL_CHOICES),
        }