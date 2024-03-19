### Directory Structure Overview

```
shopping_cart/
├── auth/
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py                   # Urls for views related to auth
│   ├── views.py                  # Views for auth module
│   ├── models/                   # User models
│   │   └── user.py               # Model for user
│   ├── serializers.py            # Serializers for auth
│   └── tests/                    # Unit tests
├── shopping_cart/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Contains settings for the project
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── apps/
    ├── products/
    │    ├── admin.py
    │    ├── apps.py
    │    ├── urls.py              # Urls for views related to product
    │    ├── views.py             # Views for product module
    │    ├── models.py            # Product models
    │    ├── serializers.py
    │    ├── services/
    │    │   └── products.py      # Business logic for product
    │    └── tests/               # Unit tests for business logic
    ├── orders/
    │    ├── admin.py
    │    ├── apps.py
    │    ├── urls.py              # Urls for views related to orders
    │    ├── views.py             # Views for orders module
    │    ├── models.py            # Order models
    │    ├── serializers.py
    │    ├── services/
    │    │   └── orders.py        # Business logic for order
    │    └── tests/               # Unit tests for business logic│
    └── payments/
         ├── admin.py
         ├── apps.py
         ├── urls.py              # Urls for views related to payment
         ├── views.py             # Views for payment module
         ├── models.py            # Payments models
         ├── serializers.py
         ├── services/
         │   └── payments.py      # Business logic for payment
         └── tests/               # Unit tests for business logic│


```