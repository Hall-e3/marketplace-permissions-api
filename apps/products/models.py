from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(TimeStampedUUIDModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        PENDING_APPROVAL = 'pending_approval', _('Pending Approval')
        APPROVED = 'approved', _('Approved')
    
    business = models.ForeignKey(
        'businesses.Business', 
        on_delete=models.CASCADE, 
        related_name='products'
    )
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='created_products'
    )
    
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.DRAFT
    )
    
    class ApprovedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Product.Status.APPROVED)

    # Custom managers
    objects = models.Manager()
    approved = ApprovedManager()

    def __str__(self):
        return self.name
        
    def submit_for_approval(self):
        if self.status == self.Status.DRAFT:
            self.status = self.Status.PENDING_APPROVAL
            self.save()
    
    def approve(self):
        if self.status == self.Status.PENDING_APPROVAL:
            self.status = self.Status.APPROVED
            self.save()
