# Repository Guidelines

## Project Structure & Module Organization
This is a Django-based real estate application organized into several specialized apps:
- **core**: Contains core logic and general views.
- **properties**: Manages property listings, builders, and related models.
- **leads**: Handles lead capture and management.
- **seo**: Manages SEO-related data.
- **kalpvriksh**: Project configuration, settings, and root URL routing.
- **templates**: Centralized directory for HTML templates.
- **static**: CSS and JavaScript assets.
- **media**: User-uploaded content like property and builder images.

## Build, Test, and Development Commands
The project uses standard Django management commands. Ensure your virtual environment is activated before running these:
- **Start Development Server**: `python manage.py runserver`
- **Apply Migrations**: `python manage.py migrate`
- **Create Migrations**: `python manage.py makemigrations`
- **Create Superuser**: `python manage.py createsuperuser`
- **Collect Static Files**: `python manage.py collectstatic`

## Coding Style & Naming Conventions
- Follow **PEP 8** guidelines for Python code.
- Uses **Django's default project structure** and naming conventions.
- Templates are located in a root `templates/` directory, organized by app name where applicable.
- **Timezone**: Set to `Asia/Kolkata`.
- **Database**: Uses SQLite for development (`db.sqlite3`).

## Testing Guidelines
- **Run all tests**: `python manage.py test`
- **Run tests for a specific app**: `python manage.py test <app_name>`
- Each app contains a `tests.py` file for unit and integration tests.
