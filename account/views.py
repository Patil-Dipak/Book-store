from django.shortcuts import render, redirect

from .forms import  RegistrationForm

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