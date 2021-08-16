from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Basket view

@login_required     # only if user is login
def BasketView(request):
    return render(request, 'payment/home.html')
