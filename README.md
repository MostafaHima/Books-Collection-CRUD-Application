# Books Collection CRUD Application

This is a simple **Books Collection CRUD** app built with **Flask** and **SQLAlchemy** for training on database management.

## Purpose
This project is a training exercise to practice **database operations** (Create, Read, Update, Delete) It helps users manage a book collection, including title, author, and rating.

## Features
- Add new books with title, author, and rating.
- View all books in the collection.
- Update the rating of an existing book.
- Delete a book from the collection.

## Technologies Used
- **Flask**: Micro web framework for Python.
- **SQLAlchemy**: ORM (Object Relational Mapper) for database management.
- **SQLite**: Lightweight database for storing book data.

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone  https://github.com/MostafaHima/Books-Collection-CRUD-Application.git
   cd Books-Collection-CRUD-Application
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python main.py
   ```
4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure
- `main.py`: Main Flask application containing routes and database models.
- `templates/`: HTML templates for rendering pages.
- `Books_collections.db`: SQLite database file.
- `requirements.txt`: List of dependencies for the project.



