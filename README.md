# Consulting_Company_Website Documentation

## Overview

This project is a consulting company website built with Django, supporting multilingual content (English, Turkish, German), responsive design, and content management via the Django admin panel. The site is deployed on AWS and available at [cafdanismanlik.com](https://cafdanismanlik.com).

---

## Project Structure

```
Consulting_Company_Website/
│
├── config/                # Django project configuration
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│   └── __init__.py
│
├── website/               # Main application
│   ├── admin.py           # Admin interface for models
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/        # Database migrations
│   ├── models.py          # Data models (categories, services, etc.)
│   ├── templates/         # Django templates
│   │   └── website/
│   │       ├── about.html
│   │       ├── category_confirm_delete.html
│   │       ├── category_detail.html
│   │       ├── category_form.html
│   │       ├── category_list.html
│   │       ├── contacts.html
│   │       └── includes/
│   │           ├── footer.html
│   │           └── header.html
│   ├── tests.py
│   ├── translation.py
│   ├── urls.py
│   └── views.py
│
├── users/                 # User management app
│   ├── admin.py
│   ├── apps.py
│   ├── management/
│   │   └── commands/
│   │       └── createadmin.py  # Command to create superuser
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── locale/                # Localization (en, tr, de)
│   ├── en/LC_MESSAGES/django.po
│   ├── tr/LC_MESSAGES/django.po
│   └── de/LC_MESSAGES/django.po
│
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   │   ├── bootstrap*.css
│   │   └── custom.css
│   ├── images/
│   │   ├── logo.jpg
│   │   ├── background-main.avif
│   │   └── ...
│   └── js/
│       └── bootstrap*.js
│
├── media/                 # User-uploaded media files
│   ├── category_backgrounds/
│   └── category_images/
│
├── nginx/                 # Nginx configuration for production
│   ├── Dockerfile
│   └── nginx.conf
│
├── templates/             # Base templates (e.g., 404.html, base.html)
│
├── .env                   # Environment variables (not committed)
├── .dockerignore
├── .flake8                # Linter settings
├── .gitignore
├── docker-compose.yml     # Docker orchestration
├── Dockerfile             # Application Dockerfile
├── LICENSE
├── manage.py              # Django management
├── pyproject.toml         # Project dependencies and settings
├── README.md
├── requirements.txt
├── uv.lock
└── ...
```

---

## Key Components

### 1. Django Apps
- **website** — Main business logic, models, templates, and views.
- **users** — User management, custom commands, migrations.

### 2. Localization
- Supports English, Turkish, and German.
- Translation files: `locale/en/LC_MESSAGES/django.po`, `locale/tr/LC_MESSAGES/django.po`, `locale/de/LC_MESSAGES/django.po`.

### 3. Templates
- Uses Django templates for page rendering.
- Main templates: `about.html`, `category_list.html`, `contacts.html`, etc.
- Includes header and footer components.

### 4. Static and Media Files
- Static files (CSS, JS, images) are in `static/`.
- User-uploaded images are in `media/`.

### 5. Docker & Deployment
- The project is containerized with Docker.
- Uses `docker-compose.yml` for orchestration.
- Nginx configuration for production is in `nginx/`.
- The site is deployed on AWS.

---

## Running and Deployment

1. **Local Development:**
   - Install dependencies:
     `pip install -r requirements.txt`
   - Apply migrations:
     `python manage.py migrate`
   - Run the server:
     `python manage.py runserver`

2. **Docker:**
   - Build and run containers:
     `docker-compose up --build`

3. **Production Deployment:**
   - AWS services are used (EC2, S3, RDS, etc.).
   - Nginx acts as a reverse proxy.
   - Domain: [cafdanismanlik.com](https://cafdanismanlik.com)

---

## Important Files

- `config/settings.py` — Main Django settings.
- `website/models.py` — Data models.
- `website/views.py` — Request handlers.
- `website/templates/website/` — Page templates.
- `static/` — Styles, scripts, images.
- `locale/` — Translations.
- `Dockerfile`, `docker-compose.yml` — Containerization.
- `nginx/nginx.conf` — Nginx config.

---

## Contact & Support

For questions, use the contact form on the website or the contact details at [cafdanismanlik.com](https://cafdanismanlik.com).