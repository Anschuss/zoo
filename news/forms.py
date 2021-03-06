from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import News


class CreateNews(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class RegistrationUserForm(UserCreationForm):
    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    class Meta:
        fields = '__all__'
