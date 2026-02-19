from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not first_name:
            raise ValueError(_("Users must have a first name"))
        if not last_name:
            raise ValueError(_("Users must have a last name"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))

        from apps.businesses.models import Business
        from apps.roles.models import Role

        business_name = extra_fields.pop('business_name', 'Default Business')
        business, _ = Business.objects.get_or_create(name=business_name)
        
        role, _ = Role.objects.get_or_create(
            name=Role.RoleType.ADMIN,
            defaults={
                'can_create_product': True,
                'can_edit_product': True,
                'can_approve_product': True,
                'can_delete_product': True,
            }
        )

        user = self.model(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            business=business,
            role=role,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))
        
        if not password:
            raise ValueError(_("Superusers must have a password"))

        return self.create_user(first_name, last_name, email, password, **extra_fields)
