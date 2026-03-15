# Django Modular Entity Mapping System

A modular backend system built with **Django** and **Django REST Framework (DRF)** to manage master entities and hierarchical mappings between them. 

This project demonstrates a clean **modular Django architecture**, manual **APIView-based API development**, and automatic **API documentation using drf-yasg (Swagger / ReDoc)**.

---

## 🎯 Project Objective

The system manages four master entities and their hierarchical relationships:
* `Vendor`
* `Product`
* `Course`
* `Certification`

And the following mappings:
* `Vendor` → `Product`
* `Product` → `Course`
* `Course` → `Certification`

Each entity and mapping is implemented as a **separate Django app** to maintain strict modular architecture.

---

## 🛠️ Tech Stack & Features

* **Python & Django**
* **Django REST Framework (APIView only)**
* **drf-yasg** (Swagger / ReDoc documentation)
* **SQLite** (default Django database)
* **Reusable Code**: Custom `get_object_or_404` utility function implemented for object fetching.
* **Strict Validation**: Duplicate prevention and single `primary_mapping` enforcement per parent constraint implemented at the serializer level.
* **Query Parameters**: Custom filter parameters via `request.GET.get` functionality.
* **Chronological Ordering**: Data lists natively order by descending `-created_at`.

---

## 📁 Project Architecture

This project follows a **modular app-based architecture** where each entity and mapping is strictly isolated.

```
project_root
│
├── modular_entity_system
│   ├── manage.py
│   ├── modular_entity_system/ (core settings)
│   ├── utils.py (shared utilities)
│   │
│   ├── vendor/
│   ├── product/
│   ├── course/
│   ├── certification/
│   │
│   ├── vendor_product_mapping/
│   ├── product_course_mapping/
│   └── course_certification_mapping/
│
├── venv/
├── requirements.txt
└── .gitignore
```

### Master Apps
Contains only core models: `id`, `name`, `code`, `description`, `is_active`, `created_at`, `updated_at`.

| App | Description |
| --- | --- |
| `vendor` | Vendor entity management |
| `product` | Product entity management |
| `course` | Course entity management |
| `certification` | Certification entity management |

### Mapping Apps
Contains mapping relationships consisting of parent/child foreign keys, `primary_mapping`, and timestamp fields.

| App | Description |
| --- | --- |
| `vendor_product_mapping` | Maps vendors to products |
| `product_course_mapping` | Maps products to courses |
| `course_certification_mapping` | Maps courses to certifications |

---

## 🌐 API Design

All endpoints are strictly constructed using manual DRF **APIView** routing. 

Supported operations:
* **GET** - List & Retrieve
* **POST** - Create 
* **PUT** - Update
* **PATCH** - Partial Update
* **DELETE** - Remove

Example routing (`/api/products/`):
* `GET /api/products/?vendor_id=X` → list products filtered by vendor
* `POST /api/products/` → create product
* `GET /api/products/<id>/` → retrieve product
* `PUT /api/products/<id>/` → update product
* `PATCH /api/products/<id>/` → partial update product
* `DELETE /api/products/<id>/` → delete product

*Similar routing applies strictly across all 7 module applications.*

---

## 📖 API Documentation

Robust API documentation automatically generated via **drf-yasg**:
* Swagger UI: `/swagger/`
* ReDoc UI: `/redoc/`

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sidhyaashu/django-modular-entity-system.git
cd django-modular-entity-system
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

**Activate the environment:**
* **Windows:** `venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
cd modular_entity_system
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server
```bash
python manage.py runserver
```

The system will now be accessible locally at `http://127.0.0.1:8000/`.

---

## ✅ Acceptance Criteria Completed

- [x] Separate Django apps mapped explicitly.
- [x] API structures written manually utilizing only `APIView`.
- [x] Reusable modular file configurations (models, serializers, urls, views, admin instances existing separately per application).
- [x] Proper CRUD logic built manually bypassing generic mixins entirely.
- [x] Complex parent-child duplicate and strict boolean `unique_together` modeling requirements implemented.
- [x] Extensive API Swagger configurations completed.
- [x] High-quality robust handling leveraging native Python HTTP configurations via custom `get_object_or_404`.

---

## 📄 License
Created for technical evaluation.
