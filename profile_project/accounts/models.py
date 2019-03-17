from django.db import models


class UserData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateTimeField()
    bio = models.TextField()

