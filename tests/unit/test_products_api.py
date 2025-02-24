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
def test_get_all_product(api_client, inventory_fixture) -> None:


    response_create = api_client.get("/api/products", format="json")
    assert response_create.status_code == 200
    assert 'product' in response_create.data[0]
    assert 'stock' in response_create.data[0]
    assert 'name' in response_create.data[0]['product']
    assert response_create.data[0]['product']['name'] == inventory_fixture.product.name
    assert response_create.data[0]['product']['sku'] == inventory_fixture.product.sku
    assert response_create.data[0]['stock'] == inventory_fixture.stock

@pytest.mark.django_db
def test_create_product(api_client) -> None:

    # Test the create Product API

    payload = {
        "product": {
            "name": "Leche",
            "sku": "SKU12345"
        }
    }

    response_create = api_client.post("/api/products", data=payload, format="json")

    assert response_create.status_code == 201
    assert response_create.data["product"]["name"] == payload["product"]["name"]
    assert response_create.data["product"]["sku"] == payload["product"]["sku"]
    assert response_create.data["stock"] == 100

@pytest.mark.django_db
def test_create_product_sku_exists(api_client, inventory_fixture) -> None:

    payload = {
        "product": {
            "name": "Leche",
            "sku": "TESTSKU1234"
        }
    }

    response_create = api_client.post("/api/products", data=payload, format="json")

    assert response_create.status_code == 400
    

@pytest.mark.django_db
def test_create_product_bad_request(api_client) -> None:

    # Test the create Product API

    payload = {
        "name": "Leche"
    }

    response_create = api_client.post("/api/products", data=payload, format="json")

    assert response_create.status_code == 400
