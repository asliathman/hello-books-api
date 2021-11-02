#BUILDING API PT 2 
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        title = request.args.get("title")
        if title:
            books = Book.query.filter_by(title=title)
        else:
            books = Book.query.all()
        
        books_response = []
        for book in books:
            #way to refactor: create a helper function create dict so this dict stuff doesn't have to live here using setattrb()
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
        
    elif request.method == "POST":
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return jsonify(f"{new_book.title} successfully added"), 201

@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
            return jsonify(f"Error: Book #{book_id} not found"), 404

    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    elif request.method == "PUT":
        form_data = request.get_json()

        book.title = form_data["title"]
        book.description = form_data["description"]

        db.session.commit()

        return make_response(f"Book #{book.id} successfully updated")
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()

        return make_response(f"Book #{book.id} successfully deleted")

    

