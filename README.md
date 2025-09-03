# 🧩 Flask User Management API

A lightweight Python Flask-based REST API for managing users (Create, Read, Update, Delete) with in-memory data storage. Includes auto-seeded user data and interactive Swagger (OpenAPI) documentation served at the root (`/`).

---

## 📦 Features

- ✅ In-memory storage for rapid development and testing  
- 🔄 Full CRUD endpoints: `POST`, `GET`, `PUT`, `DELETE`  
- 🧪 Swagger UI for testing & docs at `/` 
- 🚀 Minimal setup, ready for DevOps CI/CD pipelines  
- 🧰 Easily extendable to use persistent databases (e.g., SQLite, PostgreSQL)

---

## Getting Started

### Requirements

- Python 3
- `pip`

### Dependency Installation

```bash
pip install -r requirements.txt
```

### Run the app in development mode
```
python app.py
```
or
```
flask run
```

### Unittesting
```
pytest
```
Exports for junit reports etc. are possible

## Deployment to production
- Setup virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
- Install dependencies while in virtual environment:
```
pip install -r requirements.txt
```
- Install dedicated webserver package gunicorn:
```
pip install gunicorn
```
- Run webserver in `app` folder:
```
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```
