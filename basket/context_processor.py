from .basket import Basket

def basket(request):
    return {'basket': Basket(request)}  #Returning the session information from Basket.py