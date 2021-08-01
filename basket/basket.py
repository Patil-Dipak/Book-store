
class Basket():
    """
    A base basket class, providing some default behaviors that
    can be changed or overrided, as necessary
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        # check session is already exist or not
        if 'skey' not in request.session:
            basket = self.session['skey'] = {} # set blank

        self.basket = basket
    
    def add(self, product,  qty):
        """
        Adding and updating the user basket session data 
        """
        product_id = product.idc

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}
        self.session.modified = True 