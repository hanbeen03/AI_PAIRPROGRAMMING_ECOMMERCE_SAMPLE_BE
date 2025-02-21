# import pytest
# from fastapi.testclient import TestClient
# from app.main import app
# from app import schemas

# client = TestClient(app)

# @pytest.fixture
# def test_product():
#     return schemas.ProductCreate(name="Test Product", description="Test Description", price=10.0)

# def test_create_product(test_product):
#     response = client.post("/products/", json=test_product.dict())
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == test_product.name
#     assert data["description"] == test_product.description
#     assert data["price"] == test_product.price

# def test_read_product(test_product):
#     # First, create a product
#     create_response = client.post("/products/", json=test_product.dict())
#     product_id = create_response.json()["id"]

#     # Then, read the product
#     response = client.get(f"/products/{product_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == product_id
#     assert data["name"] == test_product.name
#     assert data["description"] == test_product.description
#     assert data["price"] == test_product.price

# def test_update_product(test_product):
#     # First, create a product
#     create_response = client.post("/products/", json=test_product.dict())
#     product_id = create_response.json()["id"]

#     # Update the product
#     updated_product = schemas.ProductUpdate(name="Updated Product", description="Updated Description", price=20.0)
#     response = client.put(f"/products/{product_id}", json=updated_product.dict())
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == product_id
#     assert data["name"] == updated_product.name
#     assert data["description"] == updated_product.description
#     assert data["price"] == updated_product.price

# def test_delete_product(test_product):
#     # First, create a product
#     create_response = client.post("/products/", json=test_product.dict())
#     product_id = create_response.json()["id"]

#     # Delete the product
#     response = client.delete(f"/products/{product_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == product_id

#     # Try to read the deleted product
#     response = client.get(f"/products/{product_id}")
#     assert response.status_code == 404

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# def test_read_product(db_session):
#     response = client.get("/api/v1/products/1")
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": 1,
#         "category_id": 1,
#         "name": "화이트 티셔츠",
#         "price": 15000.00,
#         "description": "부드러운 코튼 소재로 제작된 베이직 화이트 티셔츠. 어디에나 잘 어울리는 필수 아이템.",
#         "image_url":"https://wt6saceanewtylcm.public.blob.vercel-storage.com/tshirts_1-vh0hFouoWBQmTXewI8Ad6FoFuEDVmt.jpg"
#     }

def test_create_product_and_read_product(db_session):
    product_data = {
        "name": "New Product",
        "description": "This is a new product",
        "price": 100,
        "image_url": "https://example.com/image.jpg",
        "category_id": 2
    }

    expected_response = {
        "name": "New Product",
        "description": "This is a new product",
        "price": 100,
        "image_url": "https://example.com/image.jpg",
        "id": 1,
        "category_id": 2
    }
    response = client.post("/api/v1/products/", json=product_data)
    assert response.status_code == 200
    assert response.json() == expected_response

    #### read product

    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json() == expected_response

    ### update product
    update_data = {
        "name": "Updated Product",
        "description": "This is an updated product",
        "price": 200,
        "image_url": "https://example.com/updated_image.jpg",
        "category_id": 3
    }

    expected_response = {
        "name": "Updated Product",
        "description": "This is an updated product",
        "price": 200,
        "image_url": "https://example.com/updated_image.jpg",
        "id": 1,
        "category_id": 3
    }
    response = client.put("/api/v1/products/1", json=update_data)
    assert response.status_code == 200
    assert response.json() == expected_response

    ### delete product
    response = client.delete("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json() == expected_response

    ### read product again
    response = client.get("/api/v1/products/1")
    assert response.status_code == 404