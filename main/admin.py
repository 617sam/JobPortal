from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Job, CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'location', 'level', 'openings')
    search_fields = ('name', 'details', 'address', 'location')