from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class SignForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Номер телефона какого-то формата')

    # def clean_password(self):
    #     cleaned_data = self.cleaned_data
    #     if cleaned_data['password'] != cleaned_data['password2']:
    #         raise forms.ValidationError('Пароли не совпадают')
    #     return cleaned_data['password2']

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'email', 'password1', 'password2')

    
