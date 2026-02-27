# 🚚 Logistics & Shipment Tracking API

A scalable, event-driven logistics management backend built with **FastAPI**, supporting shipment lifecycle management, tracking, hub operations, and role-based access control.

---

# 👥 Actors

* **Customer**
* **Delivery Agent**
* **Admin**

---

# 🛠 Technology Stack

* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication
* Docker
* Redis (Tracking cache & real-time shipment status)

---

# 📂 Project Structure

```bash
logistics-api/
│
├── app/
│   ├── main.py
│
│   ├── core/                     # Core infrastructure
│   │   ├── config.py             # Environment settings
│   │   ├── database.py           # Engine, SessionLocal, Base
│   │   ├── security.py           # JWT & password hashing
│   │   ├── dependencies.py       # get_db, get_current_user, role checks
│
│   ├── models/                   # SQLAlchemy ORM models
│   │   ├── base.py
│   │   ├── user.py               # Admin, Dispatcher, Driver, Customer
│   │   ├── shipment.py
│   │   ├── tracking.py
│   │   ├── hub.py
│
│   ├── schemas/                  # Pydantic schemas
│   │   ├── auth_schema.py
│   │   ├── user_schema.py
│   │   ├── shipment_schema.py
│   │   ├── tracking_schema.py
│   │   ├── hub_schema.py
│
│   ├── repositories/             # Data access layer
│   │   ├── user_repository.py
│   │   ├── shipment_repository.py
│   │   ├── tracking_repository.py
│   │   ├── hub_repository.py
│
│   ├── services/                 # Business logic layer
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── shipment_service.py
│   │   ├── tracking_service.py
│   │   ├── hub_service.py
│
│   ├── api/                      # API layer (Controllers)
│   │   ├── router.py             # Central router
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── shipments.py
│   │   │   ├── tracking.py
│   │   │   ├── hubs.py
│   │   │   ├── admin.py
│
│   ├── middleware/
│   │   ├── cors.py
│   │   ├── logging_middleware.py
│   │   ├── rate_limiter.py
│
│   ├── exceptions/
│   │   ├── custom_exceptions.py
│   │   ├── exception_handlers.py
│
│   ├── utils/
│   │   ├── constants.py
│   │   ├── validators.py
│
├── alembic/
├── alembic.ini
│
├── tests/
│   ├── test_auth.py
│   ├── test_shipments.py
│   ├── test_tracking.py
│   ├── test_hubs.py
│   ├── test_admin.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# 🧠 Service Responsibilities (Event-Driven Architecture)

## 🔐 Auth Service

**Responsibilities:**

* User registration
* User login
* JWT token generation
* Publish user-related events

---

## 📦 Shipment Service

**Responsibilities:**

* Create shipment
* Update shipment details
* Assign delivery agent
* Change shipment status

---

## 🏢 Hub Service

**Responsibilities:**

* Create & manage hubs
* Assign shipments to hubs

---

## 📍 Tracking Service

**Responsibilities:**

* Store shipment tracking history
* Maintain Redis cache for latest shipment status
* Provide real-time tracking updates

---

## 📊 Reporting Service

**Responsibilities:**

* Analytics dashboard
* Performance metrics
* Daily operational reports
* Hub-level metrics

---

# ⚡ Architecture Pattern

* Layered Architecture

  * API Layer
  * Service Layer
  * Repository Layer
  * Database Layer

* Event-Driven Design

* Role-Based Access Control (RBAC)

* Redis Caching for real-time tracking

---
