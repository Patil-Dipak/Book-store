from django import forms
from .models import UserBase
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

# Registration Form
class RegistrationForm(forms.ModelForm):
    # for User name
    user_name = forms.CharField(label = 'Enter Username', min_length = 4 , max_length = 50 , help_text = 'Required')
    # For email
    email = forms.EmailField(max_length = 50 , help_text = 'Required', error_messages= {
        'required' : 'Sorry, you will need an email'})
    # for Password
    Password = forms.CharField(label = 'Password', widget= forms.PasswordInput)
    Password2 = forms.CharField(label = 'Repeat password', widget= forms.PasswordInput)

    # Meta Class
    model = UserBase
    fields = ('user_name', 'email', )

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name= user_name) # return the data

        if r.count(): # if count = 1
            raise forms.ValidationError("Username already exists")

        return user_name    # if count not one then return user_name

    # for Checking the password
    def clean_password2(self):
        cd = self.cleaned_data # store the method into cd
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords does not match.")
        
        return cd['password2']

    
    # for Checking the email
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email = email).exists():
            raise forms.ValidationError("Please use another Email, that is already taken")
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
