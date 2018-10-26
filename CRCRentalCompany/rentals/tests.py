from django.test import TestCase

from .models import Order
from .models import Store
from .models import Customer
from .models import Vehicle

class Order (TestCase):
    def setup(self):
        Order.objects.create(name = '')

    def test_order_id(self):
        order = Order.objects.get(id=id)
        self.assetEqual()
# Create your tests here.
