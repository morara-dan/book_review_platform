from app import db

# Association table for the many-to-many relationship between Book and Review
book_reviews = db.Table('book_reviews',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('review_id', db.Integer, db.ForeignKey('reviews.id'), primary_key=True)
)

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.id} - {self.name}>'

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publication_year = db.Column(db.Date, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    # Many-to-many relationship with reviews via the association table
    reviews = db.relationship('Review', secondary=book_reviews, back_populates='books', lazy=True)

    def __repr__(self):
        return f'<Book {self.id} - {self.title}>'

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)
    links = db.Column(db.String(500), nullable=True)
    books = db.relationship('Book', secondary=book_reviews, back_populates='reviews', lazy=True)

    def __repr__(self):
        return f'<Review {self.id} - Rating: {self.rating}>'