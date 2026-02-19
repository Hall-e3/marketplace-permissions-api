from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ['pkid', 'id', 'email', 'first_name', 'last_name', 'business', 'role', 'is_staff']
    list_display_links = ['id', 'email']
    list_filter = ['business', 'role', 'is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']
    
    fieldsets = (
        (_("Login Credentials"), {'fields': ('email', 'password')}),
        (_("Personal Information"), {'fields': ('first_name', 'last_name')}),
        (_("Business & Role"), {'fields': ('business', 'role')}),
        (_("Permissions"), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_("Important Dates"), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'business', 'role', 'is_staff', 'is_active'),
        }),
    )
