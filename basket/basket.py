from store.models import Product    # for the Product tabel
from decimal import Decimal         # for the Decimal conversion

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
            basket = self.session['skey'] = {}

        self.basket = basket
    
    def add(self, product,  qty):
        """
        Adding and updating the user basket session data 
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}
        
        self.save()

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum( int(item['qty']) for item in self.basket.values() )
    
    def __iter__(self):
        """
        Collect the product id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()    #store the all keys into product_ids
        products = Product.products.filter(id__in = product_ids)  #get the data of Produt tabel where id_in = product_ids

        basket = self.basket.copy()     #make the copy of session data

        for product in products:
            basket[str(product.id)]['product'] = product    # adding the remaning data of product into basket(session copy veriabel) 
        
        for item in basket.values():
            item['price'] = Decimal(item['price'])  # convert the str price into decimal
            item['total_price'] = item['price'] * item['qty']   # added new data into basket total_price
            yield item
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

#   delete method for delete item from basket
    def delete(self, product):
        """
        delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]   # For delete the session element
            self.save()
    
    def save(self):     # set true to modified 
        self.session.modified = True