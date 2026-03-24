from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User

class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Неверное имя пользователя или пароль')
        return cleaned_data


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'your@email.com'
    }))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Maria'
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'D.'
    }))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'tell about yourself...',
        'rows': 2
    }))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'bio']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email