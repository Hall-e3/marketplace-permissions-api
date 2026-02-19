# Baisoft Marketplace - Backend (Django)

A robust, multi-tenant backend architecture built with Django REST Framework.

## 🚀 Key Features

- **Modular Settings Architecture**: Refactored `settings.py` into a production-ready structure (`base.py`, `development.py`, `production.py`).
- **Multi-Tenant Architecture**: Implemented a `Business` model to support multiple organizations.
- **Role-Based Access Control (RBAC)**: Custom `Role` and `Permission` system with granular controls.
- **Custom User Model**: Extended `AbstractBaseUser` with UUID primary keys.
- **API v1 Versioning**: Structured endpoints under `/api/v1/`.
- **Structured Logging**: Configured console and file logging.
- **Automated Business Onboarding**: New users automatically create/link their business during registration.
- **Swagger/OpenAPI**: Interactive API documentation at `/swagger/`.

## 🛠️ Setup Instructions

### 1. Prerequisites

- Python 3.9+

### 2. Installation

```bash
cd backend
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed essential roles (Admin, Editor, Approver, Viewer)
python manage.py shell -c "from apps.roles.models import Role; [Role.objects.get_or_create(name=r, defaults={'can_create_product': True, 'can_edit_product': True, 'can_approve_product': True, 'can_delete_product': True}) for r in Role.RoleType.values]"

# Start server (Development)
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/v1/`.
Swagger documentation is available at `http://localhost:8000/swagger/`.

## 🧠 Tech Decisions & Assumptions

- **UUIDs over Sequential IDs**: Improved security and simplified data migrations.
- **Djoser for Authentication**: Standardized JWT flow following best practices.
- **Modular Settings**: High-quality configuration management across environments.
- **Local SQLite**: Used for ease of assessment, but swappable for PostgreSQL.
- **One Business per User**: A user is associated with a single business in this MVP.
