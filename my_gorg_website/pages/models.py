from django.db import models
from django.contrib.auth.models import AbstractUser
import bcrypt
from django.contrib.auth.hashers import check_password as django_check_password

class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    favorite_album = models.CharField(max_length=255, blank=True, null=True, verbose_name='Любимый альбом')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def set_password(self, raw_password):
        # Шифрование пароля bcrypt
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), salt).decode('utf-8')
    
    def check_password(self, raw_password):
        #проверяем, не является ли пароль в формате Django (PBKDF2)
        if self.password.startswith('pbkdf2_'):
            return django_check_password(raw_password, self.password)
        # иначе используем bcrypt
        try:
            return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))
        except ValueError:
            # Если bcrypt не может проверить (неверный формат), пробуем Django
            return django_check_password(raw_password, self.password)
    
    class Meta:
        db_table = 'custom_user'