### Directory Structure Overview

```
shopping_cart/
├── apps/
│   ├── users/
│   │    ├── admin.py
│   │    ├── apps.py
│   │    ├── urls.py              # Urls for views related to users
│   │    ├── views.py             # Views for users module
│   │    ├── models.py            # User models
│   │    ├── serializers.py       # Serializers for users
│   │    ├── services/
│   │    │   └── users.py         # Business logic for user
│   │    └── tests/               # Unit tests
│   ├── products/
│   │    ├── admin.py
│   │    ├── apps.py
│   │    ├── urls.py              # Urls for views related to product
│   │    ├── views.py             # Views for product module
│   │    ├── models.py            # Product models
│   │    ├── serializers.py
│   │    ├── services/
│   │    │   └── products.py      # Business logic for product
│   │    └── tests/               # Unit tests for business logic
│   ├── orders/
│   │    ├── admin.py
│   │    ├── apps.py
│   │    ├── urls.py              # Urls for views related to orders
│   │    ├── views.py             # Views for orders module
│   │    ├── models.py            # Order models
│   │    ├── serializers.py
│   │    ├── services/
│   │    │   └── orders.py        # Business logic for order
│   │    └── tests/               # Unit tests for business logic│
│   └── payments/
│        ├── admin.py
│        ├── apps.py
│        ├── urls.py              # Urls for views related to payment
│        ├── views.py             # Views for payment module
│        ├── models.py            # Payments models
│        ├── serializers.py
│        ├── services/
│        │   └── payments.py      # Business logic for payment
│        └── tests/               # Unit tests for business logic│
├── shopping_cart/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Contains settings for the project
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt

```