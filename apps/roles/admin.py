from django.contrib import admin
from .models import Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'can_create_product', 'can_edit_product', 'can_approve_product', 'can_delete_product']
