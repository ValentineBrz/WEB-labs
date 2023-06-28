from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=6,
        choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]
    )

    def __str__(self):
        return self.username


class Article(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=4000)

    def __str__(self):
        return self.text


class ConnectedUsers(models.Model):
    first_name = models.CharField(max_length=50)
    connected = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s connected at %s" % (self.first_name, self.connected)
