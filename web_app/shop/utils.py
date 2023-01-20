from shop.models import *


menu = [
    {'title': "Магазины", 'url_name': 'address'},
    {'title': "Доставка", 'url_name': 'delivery'},
    {'title': "Калькулятор", 'url_name': 'calc'}
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
