
# **Online Store API**

## **Project Overview**

The **Online Store API** is a backend solution for managing an online store's core functionalities. It provides endpoints to handle:

- **Categories**: Create, update, delete, and view product categories.
- **Products**: Manage products with information such as name, description, price, stock, and category association.
- **Orders**: Create orders, ensure stock validation, and retrieve order details.

This API is designed to be scalable, maintainable, and easily extendable for any e-commerce platform.

### **Key Features**

- **CRUD Operations**: Supports full CRUD operations for products and categories.
- **Order Management**: Allows order creation with stock validation.
- **Comprehensive Test Coverage**: Includes test cases for all core functionalities, covering edge cases.
- **Database**: Uses PostgreSQL for data storage.

## **Technologies Used**

- **Backend Framework**: Django 5.1.3, Django REST Framework
- **Database**: PostgreSQL
- **Testing**: Pytest
- **Authentication**: Django's built-in user model (for testing purposes)
- **Others**: DRF, PostgreSQL, Pytest

## **Project Structure**

```
online_store/
├── store/
│   ├── migrations/
│   ├── tests/
│   │   └── test_views.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── online_store/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## **Setup and Installation**

### **Prerequisites**

- **Python 3.12+**
- **Docker and Docker Compose**
- **PostgreSQL**

### **Local Development Setup**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Rohit-K-Gaikwad/online_store.git
   cd online_store
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run Database Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

### **Run Tests**

```bash
pytest -v
```

## **API Endpoints**

### **Category Endpoints**

| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| GET    | `/api/categories/` | List all categories      |
| POST   | `/api/categories/` | Create a new category    |
| GET    | `/api/categories/{id}/` | Retrieve a category   |
| PUT    | `/api/categories/{id}/` | Update a category     |
| DELETE | `/api/categories/{id}/` | Delete a category     |

### **Product Endpoints**

| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| GET    | `/api/products/`  | List all products        |
| POST   | `/api/products/`  | Create a new product     |
| GET    | `/api/products/{id}/` | Retrieve a product    |
| PUT    | `/api/products/{id}/` | Update a product      |
| DELETE | `/api/products/{id}/` | Delete a product      |

### **Order Endpoints**

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | `/api/orders/`   | List all orders          |
| POST   | `/api/orders/create/` | Create a new order   |

### **Sample Request (Order Creation)**

**POST** `/api/orders/create/`

```json
{
    "user": 1,
    "products": [1, 2],
    "total_amount": 150.00
}
```

### **Sample Response**

```json
{
    "id": 1,
    "user": 1,
    "products": [1, 2],
    "total_amount": 150.00,
    "created_at": "2024-11-12T12:00:00Z"
}
```

## **Testing**

- The project uses **pytest** for testing.
- The tests cover the following functionalities:
  - Creating, listing, updating, and deleting categories
  - Creating, listing, updating, and deleting products
  - Creating orders and validating stock availability

### **Run Tests**

```bash
pytest --cov=store
```

## **Contributors**

- **Your Name** - *Initial work* - [Rohit Gaikwad](https://github.com/Rohit-K-Gaikwad)
