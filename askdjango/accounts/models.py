from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
