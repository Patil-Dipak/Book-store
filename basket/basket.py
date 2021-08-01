
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