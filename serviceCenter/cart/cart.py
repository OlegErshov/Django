from django.conf import settings
from ..services.models import Issue
class Cart(object):
    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, issue, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        issue_id = str(issue.id)
        if issue_id not in self.cart:
            self.cart[issue_id] = {'quantity': 0,
                                  'price': str(issue.price)}
        if update_quantity:
            self.cart[issue_id]['quantity'] = quantity
        else:
            self.cart[issue_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

