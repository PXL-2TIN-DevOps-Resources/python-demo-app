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

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7+
- `pip`

### 📁 Installation

```bash
pip install -r requirements.txt
```

### ▶️ Run the App
```
python app.py
```
or
```
flask run
```