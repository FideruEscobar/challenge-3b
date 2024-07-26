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
        stock = 11
    )
    return inventory

@pytest.fixture
def inventory_fixture2():
    product = Product.objects.create(
        sku = 'TESTSKU2234',
        name = 'cereal'
    )
    inventory = Inventory.objects.create(
        product = product,
        stock = 11
    )
    return inventory

@pytest.mark.django_db
def test_create_orders_products(
    api_client,
    inventory_fixture,
    inventory_fixture2
    ) -> None:

    # Test the create Product API

    payload = {
            "products": [
            {
                "product_id": 1,
                "total_products": 1
            },
            {
                "product_id": 2,
                "total_products": 1
            }
        ]
    }

    response_create = api_client.post("/api/orders", data=payload, format="json")

    assert response_create.status_code == 201
    assert 'product' in response_create.data[0]
    assert 'order' in response_create.data[0]
    assert 'product' in response_create.data[1]
    assert 'order' in response_create.data[1]
    assert 'order_number' in response_create.data[0]['order']
    assert 'order_number' in response_create.data[1]['order']
    assert response_create.data[0]["product"]["id"] == payload["products"][0]["product_id"]
    assert response_create.data[1]["product"]["id"] == payload["products"][1]["product_id"]
    

@pytest.mark.django_db
def test_create_orders_products_bad_request(api_client, inventory_fixture) -> None:

    payload = {
        "product": [
            {
                "product_id": 1,
                "total_products": 1
            }
        ]
    }

    response_create = api_client.post("/api/orders", data=payload, format="json")

    assert response_create.status_code == 400