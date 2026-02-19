from django.db import models
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    class RoleType(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        EDITOR = 'editor', _('Editor')
        APPROVER = 'approver', _('Approver')
        VIEWER = 'viewer', _('Viewer')
    
    name = models.CharField(max_length=50, choices=RoleType.choices, unique=True)
    can_create_product = models.BooleanField(default=False)
    can_edit_product = models.BooleanField(default=False)
    can_approve_product = models.BooleanField(default=False)
    can_delete_product = models.BooleanField(default=False)
    
    def __str__(self):
        return self.get_name_display()
