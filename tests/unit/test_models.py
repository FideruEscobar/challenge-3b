import pytest
from tiendastres.models import Product, Inventory, Order


@pytest.fixture
def inventory_3(db):
    product = Product.objects.create(
        sku = 'TESTSKU1234',
        name = 'sopas'
    )
    inventory = Inventory.objects.create(
        product = product,
        stock = 100
    )
    return inventory

@pytest.fixture
def order_fix(db):
    order = Order.objects.create()
    return order

@pytest.mark.django_db
def test_product_str_method(inventory_3):

    product = Product()
    product.name = 'sopas'
    assert product.__str__() == inventory_3.product.name

@pytest.mark.django_db
def test_order_str_method(order_fix):

    order = Order()
    order.order_number = 'ORD0001'
    assert order.__str__() == order_fix.order_number
