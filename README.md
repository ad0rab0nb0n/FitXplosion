# FitXplosion 💪

**A Django-based fitness and workout planning web application.**

FitXplosion is a web development project designed around fitness planning and personal workout goals. It uses Django for backend functionality and includes user authentication, fitness profile information, and workout-related features.

## ✨ Features

- **User Authentication** — Sign-up and login pages.
- **Fitness Profile** — Fields for personal fitness information and goals.
- **Workout Categories** — Workout-related categories such as cardio, yoga, abs, upper body, and lower body.
- **Fitness Goal Tracking** — Support for weight-related goals and BMI information.
- **Media-rich Interface** — Images and background media for the website.
- **PDF Utilities** — ReportLab dependency for PDF generation functionality.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite for local development
- **Frontend:** Django templates and static assets
- **PDF Generation:** ReportLab
- **Environment Configuration:** python-dotenv

## 📁 Project Structure

```text
FitXplosion/
├── manage.py
├── requirements.txt
├── .gitignore
├── workoutplanner/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── workoutplannerapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── static/
│   └── images/
└── media/
    └── images/
```

## 🚀 Getting Started

### Prerequisites

- Python 3
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/ad0rab0nb0n/FitXplosion.git
cd FitXplosion
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file in the project root. Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` for your environment.

Keep `.env` and all secret values out of version control.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## 🔐 Security Notes

- Keep secrets and database credentials in environment variables.
- Do not commit `.env` files or local database files.
- Use `DEBUG=False` and configure permitted hosts before production deployment.

## 🎯 Project Goal

FitXplosion explores how a web application can bring fitness information, workout planning, and personal fitness goals into one interface.

---

Developed as a Django web development project.
