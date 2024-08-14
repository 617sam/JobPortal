from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Job, CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Company


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "role"]  # Include 'role' in list display
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'location', 'level', 'openings')
    search_fields = ('name', 'details', 'address', 'location')
    
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'address','email', 'company_size', 'category', 'website')
    search_fields = ('name', 'location', 'address','email', 'description')
    list_filter = ('category', 'company_size')
