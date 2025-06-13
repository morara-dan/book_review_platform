from app import app, db
from models import Author, Book, Review
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Authors
    author1 = Author(name="Chinua Achebe")
    author2 = Author(name="Ngugi wa Thiong'o")

    # Create Books
    book1 = Book(title="Things Fall Apart", publication_year=date(1958, 1, 1), author=author1)
    book2 = Book(title="No Longer at Ease", publication_year=date(1960, 1, 1), author=author1)
    book3 = Book(title="The River Between", publication_year=date(1965, 1, 1), author=author2)
    book4 = Book(title="A Grain of Wheat", publication_year=date(1967, 1, 1), author=author2)

    # Create Reviews
    review1 = Review(rating=5, comment="A masterpiece!", links="https://example.com/review1")
    review2 = Review(rating=4, comment="Very insightful.", links="https://example.com/review2")
    review3 = Review(rating=3, comment="Good, but a bit slow.", links="https://example.com/review3")
    review4 = Review(rating=5, comment="Loved it!", links="https://example.com/review4")
    review5 = Review(rating=2, comment="Not my style.", links="https://example.com/review5")
    review6 = Review(rating=4, comment="Well written.", links="https://example.com/review6")

    # Associate reviews with books (many-to-many)
    book1.reviews.extend([review1, review2])
    book2.reviews.append(review3)
    book3.reviews.extend([review4, review5])
    book4.reviews.append(review6)

    db.session.add_all([author1, author2, book1, book2, book3, book4, review1, review2, review3, review4, review5, review6])
    db.session.commit()

    print("Database seeded!")