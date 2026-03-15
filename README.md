# Django Modular Entity Mapping System

A modular backend system built with **Django** and **Django REST Framework (DRF)** to manage master entities and hierarchical mappings between them.

This project demonstrates a clean **modular Django architecture**, manual **APIView-based API development**, and automatic **API documentation using drf-yasg (Swagger / ReDoc)**.

---

# Project Objective

The system manages four master entities and their hierarchical relationships:

* Vendor
* Product
* Course
* Certification

And the following mappings:

* Vendor → Product
* Product → Course
* Course → Certification

Each entity and mapping is implemented as a **separate Django app** to maintain modular architecture.

---

# Tech Stack

* Python
* Django
* Django REST Framework
* drf-yasg (Swagger API documentation)
* SQLite (default Django database)

---

# Project Architecture

This project follows a **modular app-based architecture** where each entity and mapping is implemented in its own Django app.

```
project_root
│
├── modular_entity_system
│   ├── manage.py
│   ├── modular_entity_system
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── vendor
│   ├── product
│   ├── course
│   ├── certification
│   │
│   ├── vendor_product_mapping
│   ├── product_course_mapping
│   └── course_certification_mapping
│
├── venv
├── requirements.txt
└── .gitignore
```

---

# Django Apps

## Master Apps

| App           | Description                     |
| ------------- | ------------------------------- |
| vendor        | Vendor entity management        |
| product       | Product entity management       |
| course        | Course entity management        |
| certification | Certification entity management |

---

## Mapping Apps

| App                          | Description                    |
| ---------------------------- | ------------------------------ |
| vendor_product_mapping       | Maps vendors to products       |
| product_course_mapping       | Maps products to courses       |
| course_certification_mapping | Maps courses to certifications |

---

# API Design

Each module provides the following APIs using **APIView**:

* List
* Create
* Retrieve
* Update
* Partial Update
* Delete

Example endpoints:

```
GET /api/vendors/
POST /api/vendors/

GET /api/products/
POST /api/products/

GET /api/courses/
POST /api/courses/

GET /api/certifications/
POST /api/certifications/
```

Mapping APIs will also follow the same structure.

---

# API Documentation

API documentation is generated using **drf-yasg**.

Available endpoints:

```
/swagger/
/redoc/
```

These interfaces allow developers to explore and test APIs interactively.

---

# Setup Instructions

## 1. Clone the Repository

```
git clone https://github.com/sidhyaashu/django-modular-entity-system.git
cd django-modular-entity-system
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Apply Migrations

```
cd modular_entity_system
python manage.py migrate
```

---

## 5. Run Development Server

```
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

# Development Status

Project setup completed:

* Django project initialized
* Modular apps created
* Virtual environment configured
* Dependencies installed
* Project structure established

Next development steps include:

* Implement master models
* Implement mapping models
* Create serializers
* Develop APIViews
* Add validation logic
* Configure Swagger documentation

---

# Key Learning Objectives

This project demonstrates:

* Modular Django architecture
* API development using **APIView**
* Manual request handling in DRF
* Model relationship management
* Validation and error handling
* Query parameter filtering
* API documentation with Swagger

---

# License

This project is created for educational and internship evaluation purposes.
