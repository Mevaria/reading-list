"""Reading list: a small Flask app used as the test surface for the dev pipeline."""

from flask import Flask, jsonify, render_template, request


def create_app():
    app = Flask(__name__)
    books = []
    next_id = {"value": 1}

    def find_book(book_id):
        return next((book for book in books if book["id"] == book_id), None)

    @app.get("/")
    def index():
        return render_template("index.html", books=books)

    @app.get("/api/books")
    def list_books():
        return jsonify(books)

    @app.post("/api/books")
    def add_book():
        payload = request.get_json(silent=True) or {}
        title = payload.get("title")
        author = payload.get("author", "")
        if title is None:
            return jsonify({"error": "Title is required"}), 400
        book = {
            "id": next_id["value"],
            "title": title,
            "author": author,
            "is_read": False,
        }
        next_id["value"] += 1
        books.append(book)
        return jsonify(book), 201

    @app.post("/api/books/<int:book_id>/read")
    def mark_read(book_id):
        book = find_book(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        book["is_read"] = True
        return jsonify(book)

    @app.post("/api/books/<int:book_id>/unread")
    def mark_unread(book_id):
        book = find_book(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        book["is_read"] = False
        return jsonify(book)

    return app


if __name__ == "__main__":
    create_app().run(debug=False)
