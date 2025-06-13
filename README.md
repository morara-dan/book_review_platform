# Book Review Platform

A simple Flask-SQLAlchemy application for managing authors, books, and reviews.

## Features

- **Authors**: Create and manage authors.
- **Books**: Add, update, view, and delete books. Each book belongs to an author.
- **Reviews**: Add reviews to books (many-to-many relationship).
- **API Endpoints**: RESTful routes for CRUD operations.
- **Database Migrations**: Managed with Flask-Migrate.
- **Database Seeding**: Seed script to populate sample data.
- **HTML Templates**: Basic homepage using Flask templates.

## Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd book_review_platform
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**  
   ```bash
   flask db upgrade
   ```

4. **Seed the database**  
   ```bash
   python seed.py
   ```

5. **Start the Flask app**  
   ```bash
   flask run
   ```

6. **Visit the app**  
   Open [http://localhost:5000](http://localhost:5000) in your browser.

## API Endpoints

- `GET /books` — List all books with authors and reviews
- `GET /books/<id>` — Get a specific book with author and reviews
- `POST /books` — Add a new book (with author)
- `PATCH /books/<id>` — Update a book’s details or author
- `DELETE /books/<id>` — Delete a book and its orphaned reviews

## Project Structure

- `app.py` — Main Flask application
- `models.py` — SQLAlchemy models
- `seed.py` — Database seeding script
- `templates/` — HTML templates

---

**Enjoy exploring and extending the Book Review Platform!**