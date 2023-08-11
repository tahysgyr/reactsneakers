from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'required': True}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'required': True}))
    password2 = forms.CharField(label='Подтверждение пароля',widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'required': True}))
    email = forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True}))

    def __str__(self) -> str:
        return f'{self.username} {self.password1} {self.password2} {self.email}'

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
