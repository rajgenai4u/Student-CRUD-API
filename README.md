# Student CRUD API

A fast, lightweight RESTful API for managing student records using **FastAPI**, **SQLAlchemy**, and a **Neon PostgreSQL** database.

This project implements dynamic partial updates (PATCH-like behavior on PUT), robust raw SQL query execution, custom request payload validation via Pydantic, and comprehensive HTTP status error handling.

---

## 📋 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup and Installation](#-setup-and-installation)
- [Environment Variables](#-environment-variables)
- [Database Setup](#-database-setup)
- [Running the Application](#-running-the-application)
- [API Documentation & Endpoints](#-api-documentation--endpoints)
- [Detailed Code Explanation](#-detailed-code-explanation)

---

## ✨ Features
- **Database Health Check:** Automatically verifies the database connection on startup.
- **Strict Data Validation:** Validates emails, age bounds, and string lengths before reaching the database.
- **Dynamic Partial Updates:** Allows updating individual fields without overwriting unset fields with `NULL`.
- **Accurate HTTP Status Codes:** Returns `201 Created` for creations, `404 Not Found` for missing resources, and `400 Bad Request` for invalid requests.
- **SQL Injection Prevention:** Uses parameterized SQL bindings for all query executions.

---

## 🛠 Tech Stack
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** [Neon PostgreSQL](https://neon.tech/)
- **ORM / Database Access:** [SQLAlchemy](https://www.sqlalchemy.org/) (Core & Raw SQL Execution)
- **Data Validation:** [Pydantic v2](https://docs.pydantic.dev/)
- **Environment Management:** [python-dotenv](https://github.com/theskumar/python-dotenv)
- **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)

---

## 📁 Project Structure

```text
Student-CRUD-API/
│
├── studcrud.py          # Main application code (routes, models, DB connection)
├── .env                 # Environment variables (Database URL)
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
