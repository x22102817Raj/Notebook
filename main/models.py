from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class Article(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text')
    author = models.CharField('Author', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' by ' + self.author





