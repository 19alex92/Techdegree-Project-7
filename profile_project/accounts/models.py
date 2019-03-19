from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    date_of_birth = models.DateField(blank=True, default='')
    favorite_animal = models.CharField(max_length=255, blank=True, default='')
    favorite_food = models.CharField(max_length=300, blank=True, default='')
    hobby = models.CharField(max_length=300, blank=True, default='')
    bio = models.TextField(blank=True, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return "Profile of {}".format(self.first_name)