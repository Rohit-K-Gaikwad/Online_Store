import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from store.models import Category, Product, Order
from django.contrib.auth.models import User

# Initialize API client
client = APIClient()

@pytest.fixture
def create_user():
    """Fixture to create a test user."""
    user = User.objects.create_user(username="testuser", password="password")
    return user

@pytest.fixture
def create_category():
    """Fixture to create a test category."""
    category = Category.objects.create(name="Electronics", description="Electronic devices")
    return category

@pytest.fixture
def create_product(create_category):
    """Fixture to create a test product."""
    product = Product.objects.create(
        name="Smartphone",
        description="Latest model",
        price=699.99,
        stock=10,
        category=create_category
    )
    return product

@pytest.mark.django_db
def test_create_category():
    """Test for creating a category."""
    url = reverse('category-list-create')
    data = {"name": "Books", "description": "Various types of books"}
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['name'] == "Books"

@pytest.mark.django_db
def test_list_categories(create_category):
    """Test for listing categories."""
    url = reverse('category-list-create')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) > 0

@pytest.mark.django_db
def test_update_category(create_category):
    """Test for updating a category."""
    url = reverse('category-detail', args=[create_category.id])
    data = {"name": "Updated Electronics", "description": "Updated description"}
    response = client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data['name'] == "Updated Electronics"

@pytest.mark.django_db
def test_delete_category(create_category):
    """Test for deleting a category."""
    url = reverse('category-detail', args=[create_category.id])
    response = client.delete(url)
    assert response.status_code == 204

@pytest.mark.django_db
def test_create_product(create_category):
    """Test for creating a product."""
    url = reverse('product-list-create')
    data = {
        "name": "Laptop",
        "description": "High performance",
        "price": 1500.00,
        "stock": 5,
        "category": create_category.id
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['name'] == "Laptop"

@pytest.mark.django_db
def test_list_products(create_product):
    """Test for listing products."""
    url = reverse('product-list-create')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) > 0

@pytest.mark.django_db
def test_update_product(create_product):
    """Test for updating a product."""
    url = reverse('product-detail', args=[create_product.id])
    data = {
        "name": "Updated Smartphone",
        "description": "Updated model",
        "price": 799.99,
        "stock": 8,
        "category": create_product.category.id
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data['name'] == "Updated Smartphone"

@pytest.mark.django_db
def test_delete_product(create_product):
    """Test for deleting a product."""
    url = reverse('product-detail', args=[create_product.id])
    response = client.delete(url)
    assert response.status_code == 204

@pytest.mark.django_db
def test_create_order(create_user, create_product):
    """Test for creating an order with sufficient stock."""
    url = reverse('order-create')
    data = {
        "user": create_user.id,
        "products": [create_product.id],
        "total_amount": create_product.price
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['total_amount'] == str(create_product.price)

@pytest.mark.django_db
def test_create_order_insufficient_stock(create_user, create_product):
    """Test for creating an order with insufficient stock."""
    create_product.stock = 0
    create_product.save()

    url = reverse('order-create')
    data = {
        "user": create_user.id,
        "products": [create_product.id],
        "total_amount": create_product.price
    }
    response = client.post(url, data, format='json')

    # Assert status code
    assert response.status_code == 400

    # Check if the actual error message contains 'out of stock'
    assert "out of stock" in response.data['error'].lower()

@pytest.mark.django_db
def test_create_order_multiple_products(create_user, create_category):
    """Test for creating an order with multiple products."""
    product1 = Product.objects.create(
        name="Headphones",
        description="Noise cancelling",
        price=199.99,
        stock=5,
        category=create_category
    )
    product2 = Product.objects.create(
        name="Keyboard",
        description="Mechanical",
        price=99.99,
        stock=10,
        category=create_category
    )
    
    url = reverse('order-create')
    total_amount = product1.price + product2.price
    data = {
        "user": create_user.id,
        "products": [product1.id, product2.id],
        "total_amount": total_amount
    }
    
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert float(response.data['total_amount']) == total_amount


@pytest.mark.django_db
def test_order_list(create_user, create_product):
    """Test for listing orders."""
    # Create a test order
    Order.objects.create(user=create_user, total_amount=create_product.price)

    # Use the correct list endpoint
    url = reverse('order-list')
    response = client.get(url)
    
    # Assert status code and check response
    assert response.status_code == 200
    assert len(response.data) > 0

