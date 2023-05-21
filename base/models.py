from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name


class UserModel(models.Model):
    company = models.ManyToManyField(Company, related_name="users")
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=250, unique=True)

    def __str__(self):
        return self.username
