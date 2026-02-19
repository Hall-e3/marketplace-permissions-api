from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.businesses.models import Business
from apps.roles.models import Role

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_business_and_role(sender, instance, created, **kwargs):
    if created:
        if not instance.business:
            business_name = f"{instance.first_name}'s Business" if instance.first_name else f"{instance.email.split('@')[0]}'s Business"
            business = Business.objects.create(name=business_name)
            instance.business = business
            
        if not instance.role:
            admin_role, _ = Role.objects.get_or_create(
                name=Role.RoleType.ADMIN,
                defaults={
                    'can_create_product': True,
                    'can_edit_product': True,
                    'can_delete_product': True,
                    'can_approve_product': True,
                }
            )
            instance.role = admin_role
            
        instance.save()
