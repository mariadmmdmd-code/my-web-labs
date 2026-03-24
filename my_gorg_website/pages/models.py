from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    bio = models.TextField(null=True, blank=True, verbose_name='about')
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'