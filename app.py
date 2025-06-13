from datetime import datetime
from flask import Flask, request, jsonify, abort, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Author, Book, Review

@app.route('/')
def index():
    return "Welcome to the Book Review API!"

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = []
    for book in books:
        books_list.append({
            "id": book.id,
            "title": book.title,
            "publication_year": book.publication_year.isoformat() if book.publication_year else None,
            "author": book.author.name if book.author else None,
            "reviews": [
                {
                    "id": review.id,
                    "rating": review.rating,
                    "comment": review.comment,
                    "links": review.links
                }
                for review in book.reviews
            ]
        })
    return jsonify(books_list)
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.filter_by(id=id).first()

    if not book:
        return make_response(jsonify({"error": f"Book with ID {id} not found"}), 404)

    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"error": f"An error occurred while deleting the book: {str(e)}"}), 500)

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    publication_year = data.get('publication_year')
    author_id = data.get('author_id')
    if not title or not author_id:
        return jsonify({"error": "Title and author_id are required"}), 400
    pub_year = datetime.strptime(publication_year, "%Y-%m-%d").date() if publication_year else None
    book = Book(title=title, publication_year=pub_year, author_id=author_id)
    db.session.add(book)
    db.session.commit()

    return jsonify({
        "id": book.id,
        "title": book.title,
        "publication_year": book.publication_year.isoformat() if book.publication_year else None,
        "author_id": book.author_id
    }), 201

@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    book = Book.query.filter_by(id=id).first()
    if not book:
        return make_response(jsonify({"error": f"Book with ID {id} not found"}), 404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"errors": ["No data provided for update"]}), 400)
    try:
        if 'title' in data and isinstance(data['title'], str):
            book.title = data['title']
        if 'publication_year' in data and isinstance(data['publication_year'], str):
            book.publication_year = datetime.strptime(data['publication_year'], "%Y-%m-%d").date()
        db.session.commit()
        return jsonify({
            "id": book.id,
            "title": book.title,
            "publication_year": book.publication_year.isoformat() if book.publication_year else None,
            "author_id": book.author_id
        }), 200
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"error": f"An error occurred while updating the book: {str(e)}"}), 500)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= 5000, debug=True)