# AI-Kata-Sweet-Shop-Management-System
FastAPI-based Sweet Shop Management System with JWT, Cart &amp; Orders
# 🍬 AI-Kata Sweet Shop Management System

A **full-stack Sweet Shop Management System** built with **FastAPI (Python)** and a **web-based frontend**, designed to simulate a real-world business application with authentication, orders, and documented APIs.

This project is **fully executed on Windows**, includes **live backend logs**, **working APIs**, and **functional frontend screens** — not just code.

---

## 📖 About the Project

The **AI-Kata Sweet Shop Management System** represents a modern backend-driven application where users can:

- Authenticate securely
- Interact with products
- Place and view orders
- Consume APIs documented using Swagger

The goal of this project is to demonstrate **practical backend engineering**, **clean architecture**, and **frontend-backend integration**, rather than only basic CRUD operations.

---

## 🎯 Why This Project Matters

✔ Uses **FastAPI**, a modern high-performance backend framework  
✔ Implements **JWT-based authentication**  
✔ Includes **real execution proof**, not mock screenshots  
✔ Demonstrates **industry-relevant architecture**  
✔ Clean GitHub presentation suitable for **company submissions**

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **JWT Authentication**
- **Uvicorn**

### Frontend
- **HTML**
- **CSS**
- **JavaScript**

### Tools & Platform
- **Swagger UI**
- **Git & GitHub**
- **Windows OS**

---

## 🚀 Project Execution (REAL OUTPUT)

### 🖥️ Backend Running Successfully

![Backend Running](screenshots/terminal-proof.jpg)

The FastAPI backend is running successfully using **Uvicorn**, listening on:

http://127.0.0.1:8000

yaml
Copy code

This confirms:
- Application startup completed
- No runtime errors
- Backend is production-ready

---

### 📘 Swagger API Documentation (Users & Items)

![Swagger API](screenshots/api-proof-1.jpg)

FastAPI automatically generates interactive API documentation using **Swagger UI**, displaying:
- Users APIs
- Items APIs
- Authentication logic

This allows real-time API testing directly from the browser.

---

### 🔍 Swagger API – Item Read & Update Operations

![Swagger Item API](screenshots/api-proof-2.jpg)

This screen shows:
- GET operations
- PUT operations
- Request body schemas
- Live API responses

A clear demonstration of RESTful API design.

---

### 🔐 Login Page (Frontend)

![Login Page](screenshots/login-page-proof.jpg)

The login interface enables users to:
- Enter credentials
- Authenticate via backend APIs
- Access protected features

---

### 📦 Orders Page (Frontend)

![Orders Page](screenshots/orders-page-proof.jpg)

The orders screen displays:
- Order listing layout
- Status-oriented UI
- Integration readiness with backend order APIs

---

## 📂 Project Structure

AI-Kata-Sweet-Shop-Management-System/
│
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── utils.py
│ ├── dependencies.py
│ └── routers/
│ ├── auth.py
│ ├── products.py
│ ├── orders.py
│ └── cart.py
│
├── frontend/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── orders.html
│ ├── cart.html
│ └── assets/
│ ├── css/
│ └── js/
│
├── screenshots/
├── .gitignore
└── README.md

yaml
Copy code

---

## ⚙️ How to Run the Project

### ▶ Backend Setup

```bash
uvicorn main:app --reload
Open Swagger UI:

arduino
Copy code
http://127.0.0.1:8000/docs
▶ Frontend Setup
bash
Copy code
python -m http.server 5500
Open in browser:

bash
Copy code
http://localhost:5500/index.html
🧠 Key Concepts Demonstrated
RESTful API development using FastAPI

JWT-based authentication

Database modeling with SQLAlchemy

API documentation with Swagger UI

Frontend-backend integration

Clean modular project structure

Version control with Git & GitHub

🔮 Future Enhancements
Full cart functionality

Admin dashboard

Payment gateway integration

Order status tracking

Responsive UI

Cloud deployment (Render / AWS / Railway)

Dockerization

🧑‍💻 Author
Hridaya Madaan
Computer Science Engineering Student
GitHub: https://github.com/hridaya-madaan

