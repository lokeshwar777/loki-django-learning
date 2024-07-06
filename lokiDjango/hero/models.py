from django.db import models
from django.utils import timezone
# Create your models here.
class HeroType(models.Model):
    HERO_TYPE_CHOICE = [
        ('CA','CAPTAIN AMERICA'),
        ('IM','IRON MAN'),
        ('TH','THOR'),
        ('SM','SPIDERMAN')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hero/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=HERO_TYPE_CHOICE)
    description = models.TextField(default='')

def __str__(self):
    return self.name
