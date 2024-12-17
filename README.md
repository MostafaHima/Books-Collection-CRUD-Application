# Books Collection CRUD Application

This project is a simple **Books Collection CRUD** (Create, Read, Update, Delete) application built using **Flask** and **SQLAlchemy**. It allows users to manage a collection of books with details such as title, author, and rating.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Routes Overview](#routes-overview)

---

## Features
- **Add New Book**: Add books with details like title, author, and rating.
- **View All Books**: Display all the books stored in the database.
- **Edit Book Rating**: Update the rating of a book.
- **Delete Book**: Remove a book from the database.
- **User-friendly Interface**: Simple and clean HTML forms for interaction.

---

## Technologies Used
- **Flask**: Micro web framework for Python.
- **SQLAlchemy**: ORM for managing database operations.
- **SQLite**: Lightweight database for data storage.
- **HTML**: Templates for user interaction.

---

## Setup Instructions
Follow these steps to run the application on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MostafaHima/Books-Collection-CRUD-Application.git
   cd Books-Collection-CRUD-Application
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**:
   ```bash
   python main.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

---

## Routes Overview

| **Route**               | **Method** | **Description**                   |
|-------------------------|------------|-----------------------------------|
| `/`                     | `GET`      | Display all books in the database.|
| `/add`                  | `POST/GET` | Add a new book to the collection. |
| `/edit/<int:index>`     | `POST/GET` | Update the rating of a book.      |
| `/delete?id=<book_id>`  | `GET`      | Delete a book by its ID.          |



