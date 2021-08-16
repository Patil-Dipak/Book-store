from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket    # for the use Basket class 

# Basket view

@login_required     # only if user is login
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    return render(request, 'payment/home.html')
