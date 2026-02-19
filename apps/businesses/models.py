from autoslug import AutoSlugField
from django.db import models
from apps.common.models import TimeStampedUUIDModel

class Business(TimeStampedUUIDModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
