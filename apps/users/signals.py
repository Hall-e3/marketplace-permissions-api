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
            pass
