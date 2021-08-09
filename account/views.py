from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from .forms import RegistrationForm
from .tokens import account_activation_token
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode




from .models import UserBase


def account_register(request):

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        registrationForm = RegistrationForm(request.POST)

        if registrationForm.is_valid(): # Check registration is valid or not
            user = registrationForm.save(commit = False)
            user.email = registrationForm.cleaned_data['email']
            user.set_password(registrationForm.cleaned_data['password'])
            user.is_active = False  # set user active as false
            user.save() # save the user data

            # setup email

            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user':user,
                'domain': current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user),
            })

            user.email_user(subject = subject, message = message)
    
    # method is not Post
    else:
        registrationForm = RegistrationForm()
        return render(request, 'account/registration/register.html', {'form': registrationForm})

def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk = uid)
    except:
        pass
        
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')