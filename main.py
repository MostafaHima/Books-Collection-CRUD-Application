from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Float, String, Integer

# Define a base class for SQLAlchemy using DeclarativeBase
class Base(DeclarativeBase):
    pass

# Initialize the Flask app
app = Flask(__name__)

# Configure SQLAlchemy database URI (SQLite in this case)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Books_collections.db"

# Initialize SQLAlchemy with the app
# This allows us to interact with the database
db = SQLAlchemy(model_class=Base)
db.init_app(app=app)

# Define the 'Books' table/model
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key column
    title: Mapped[str] = mapped_column(String(250), nullable=True, unique=False)  # Title of the book
    author: Mapped[str] = mapped_column(String(250), unique=False)  # Author of the book
    rating: Mapped[float] = mapped_column(Float, unique=False)  # Rating of the book

# Create all tables in the database (run this within the app context)
with app.app_context():
    db.create_all()

# Route to display all books in the database
@app.route('/')
def home():
    # Fetch all books and count the total number of books
    check_data_base = db.session.query(Books).count()
    display_data_base = db.session.query(Books).all()

    # Render the home page with the list of books
    return render_template("index.html", book=display_data_base, len_books=check_data_base)

# Route to add a new book to the database
@app.route("/add", methods=["POST", "GET"])
def add():
    # Get form data for title, author, and rating
    title = request.form.get('title')
    author = request.form.get("book_author")
    rating = request.form.get("rating")

    # Check if all form inputs are provided
    if title is not None and author is not None and rating is not None:
        with app.app_context():
            # Create a new book object and add it to the database
            add_new_book = Books(title=title, author=author, rating=rating)
            db.session.add(add_new_book)
            db.session.commit()
            return redirect(url_for("home"))  # Redirect to the home route

    # Render the form to add a new book
    return render_template("add.html")

# Route to edit the rating of an existing book
@app.route("/edit/<int:index>", methods=["POST", "GET"])
def edit(index):
    # Fetch the book to be updated based on its ID
    update_rating = db.session.execute(db.select(Books).where(Books.id == index)).scalar()

    if update_rating:
        # Get new rating from the form input
        new_rating = request.form.get("new_rating")
        if new_rating:
            # Update the rating and commit the change
            update_rating.rating = new_rating
            db.session.commit()
            return redirect(url_for("home"))

    # Fetch book details to display in the edit form
    display_info_book = db.session.execute(db.select(Books).where(Books.id == index)).scalar()
    return render_template('edit.html', index=index, display=display_info_book)

# Route to delete a book from the database
@app.route("/delete")
def delete():
    # Get the book ID from the request parameters
    book_id = request.args.get("id")

    # Fetch the book object based on the ID
    delete_book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    if delete_book is not None:
        # Delete the book and commit the changes
        db.session.delete(delete_book)
        db.session.commit()
        return redirect(url_for("home"))  # Redirect to the home route

# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
