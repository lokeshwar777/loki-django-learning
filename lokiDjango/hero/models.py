from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


# one to many

class HeroReview(models.Model):
    hero = models.ForeignKey(HeroType, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review fro {self.hero.name}'

# many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    hero_types = models.ManyToManyField(HeroType, related_name='stores')

    def __str__(self):
        return self.name

# one to one 

class HeroCeritficate(models.Model):
    hero = models.OneToOneField(HeroType, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.hero}'
    