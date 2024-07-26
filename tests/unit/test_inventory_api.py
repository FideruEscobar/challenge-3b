import pytest
from tiendastres.models import Product, Inventory

@pytest.fixture
def inventory_fixture():
    product = Product.objects.create(
        sku = 'TESTSKU1234',
        name = 'galletas'
    )
    inventory = Inventory.objects.create(
        product = product,
        stock = 10
    )
    return inventory

@pytest.mark.django_db
def test_update_stock_product(api_client, inventory_fixture)-> None:

    payload = {
        "stock": 100
    }

    response_update = api_client.patch(f"/api/inventories/product/{inventory_fixture.product.id}", data=payload, format="json")

    assert response_update.status_code == 200
    assert response_update.data["message"] == "Stock of product update successfully"

@pytest.mark.django_db
def test_update_stock_bad_request(api_client, inventory_fixture) -> None:

    payload = {
    }

    response_update = api_client.patch(f"/api/inventories/product/{inventory_fixture.product.id}", data=payload, format="json")

    assert response_update.status_code == 400
