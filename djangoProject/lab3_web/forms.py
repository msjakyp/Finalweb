from django import forms
from string import Template
from django.utils.safestring import mark_safe
from .models import Articles
from django.forms import ModelForm, fields, TextInput, widgets, Textarea, ImageField, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'price','picture']

        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Product name'
            }),
            'price':Textarea(attrs={
                'class':'form-control',
                'placeholder':'Product description'
            }),
            'picture':FileInput(attrs={'class':'form-control-file'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]