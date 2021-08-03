from django.shortcuts import render, get_object_or_404

from .basket import Basket
from store.models import Product

from django.http import JsonResponse

# Create your views here.


def basket_summary(request):
    basket = Basket(request)    # create the object of basket class 
    return render(request, 'store/basket/summary.html', {'basket' : basket})

def basket_add(request):
    basket = Basket(request)    #object of Basket class 
    if request.POST.get('action') == 'post':    # check for post methods
        product_id = int(request.POST.get('productid')) # get id from the json code 
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id = product_id)
        basket.add(product = product, qty = product_qty)   # called the add method of basket class 

        basketqty = basket.__len__()
        response = JsonResponse({'qty':basketqty})
        return response