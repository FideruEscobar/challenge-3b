import pytest
from tiendastres.models import Product, Inventory

import logging

logger = logging.getLogger('django')


@pytest.fixture
def inventory_low_stock(db):
    product = Product.objects.create(
        sku = 'TESTSKU1234',
        name = 'galletas'
    )
    inventory = Inventory.objects.create(
        product = product,
        stock = 9
    )
    return inventory

@pytest.mark.django_db
def test_low_stock_product_alert(mocker, inventory_low_stock):
    
    mock_logger = mocker.patch('tiendastres.signals.logger')

    mock_logger.info.assert_called_with(f"Este producto {inventory_low_stock.product.id} tiene un stock inferior a 10")
