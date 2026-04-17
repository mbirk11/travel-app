# 🌍 Travel App (Django Project)

A simple Django-based web application for managing travel plans.  
Users can create, view, update, and delete trips, as well as explore their travel experiences.

---

## 🚀 Features

- Create new trips  
- View all trips  
- View trip details  
- Update trip information  
- Delete trips  
- User profile page  
- Simple search functionality  

---

## 🛠️ Tech Stack

- Python 3  
- Django  
- SQLite  
- Docker  
- Docker Compose  

---

## 📂 Project Structure

```
travel_app/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── db.sqlite3
├── tasks/
└── travel_app/
```

---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/mbirk11/travel-app.git
cd travel-app
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start development server

```bash
python manage.py runserver
```

### 6. Open in browser

```
http://localhost:8000
```

---

## 🐳 Run with Docker

```bash
docker compose up --build
```

Then open:

```
http://localhost:8000
```

---

## 🔍 Usage

- Homepage displays all trips  
- Click on a trip to see details  
- Create new trip using the "Create" option  
- Edit or delete trips from detail page  
- Use search to filter trips  
- Visit profile page to see user-related data  

---

## ⚠️ Notes

- This project is for educational purposes  
- SQLite is used as default database  
- Make sure Docker is running before using Docker commands  

---

## 👩‍💻 Author


