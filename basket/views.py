from django.shortcuts import render, get_object_or_404

from .basket import Basket

# Create your views here.


def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)    #object of Basket class 
    if request.POST.get('action') == 'post':    # check for post methods
        product_id = int(request.POST.get('productid')) # get id from the json code 
        product = get_object_or_404(Product, id = product_id)
        basket.add(product = product)   # called the add method of basket class 