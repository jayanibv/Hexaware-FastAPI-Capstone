Logistics & Shipment Tracking API

##Actors
• Customer
• Delivery Agent
• Admin

##Technology Stack
• FastAPI
• SQLAlchemy
• PostgreSQL
• JWT Authentication
• Docker
• Redis (for tracking cache & real-time status updates)

##Project Structure
logistics-api/
│
├── app/
│ ├── main.py
│
│ ├── core/ # Core infrastructure
│ │ ├── config.py # Environment settings
│ │ ├── database.py # Engine, SessionLocal, Base
│ │ ├── security.py # JWT, password hashing
│ │ ├── dependencies.py # get_db, get_current_user, role checks
│
│ ├── models/ # SQLAlchemy ORM models
│ │ ├── base.py
│ │ ├── user.py # Admin, Dispatcher, Driver, Customer
│ │ ├── shipment.py
│ │ ├── tracking.py
│ │ ├── hub.py
│
│ ├── schemas/ # Pydantic request/response models
│ │ ├── auth_schema.py
│ │ ├── user_schema.py
│ │ ├── shipment_schema.py
│ │ ├── tracking_schema.py
│ │ ├── hub_schema.py
│
│ ├── repositories/ # Data access layer (DB only)
│ │ ├── user_repository.py
│ │ ├── shipment_repository.py
│ │ ├── tracking_repository.py
│ │ ├── hub_repository.py
│
│ ├── services/ # Business logic layer
│ │ ├── auth_service.py
│ │ ├── user_service.py
│ │ ├── shipment_service.py
│ │ ├── tracking_service.py
│ │ ├── hub_service.py
│
│ ├── api/ # API layer (Controllers)
│ │ ├── router.py # Central router inclusion
│ │ ├── routes/
│ │ │ ├── auth.py
│ │ │ ├── shipments.py
│ │ │ ├── tracking.py
│ │ │ ├── hubs.py
│ │ │ ├── admin.py
│
│ ├── middleware/ # Middleware components
│ │ ├── cors.py
│ │ ├── logging_middleware.py
│ │ ├── rate_limiter.py # Optional (API protection)
│
│ ├── exceptions/ # Centralized error handling
│ │ ├── custom_exceptions.py
│ │ ├── exception_handlers.py
│
│ ├── utils/ # Utility helpers
│ │ ├── constants.py
│ │ ├── validators.py
│
├── alembic/ # DB migrations
├── alembic.ini
│
├── tests/ # Unit & integration tests
│ ├── test_auth.py
│ ├── test_shipments.py
│ ├── test_tracking.py
│ ├── test_hubs.py
│ ├── test_admin.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md

##Service Responsibilities (Event-Driven)
-> Auth Service
Responsibilities
• Register
• Login
• JWT creation
• Publish user events

-> Shipment Service
Responsibilities
• Create shipment
• Update shipment
• Assign agent
• Change shipment status

-> Hub Service
Responsibilities
• Manage hubs
• Assign shipments to hubs

-> Tracking Service
Responsibilities
• Store tracking history
• Maintain Redis cache for latest shipment status

-> Reporting Service
Responsibilities
• Analytics
• Performance metrics
• Daily reports
• Hub metrics

