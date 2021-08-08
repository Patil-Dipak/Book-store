from django import forms
from .models import UserBase


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

