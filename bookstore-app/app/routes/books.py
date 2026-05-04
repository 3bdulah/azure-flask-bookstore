from flask import request, jsonify, render_template, redirect, url_for, current_app
from bson import ObjectId
from app.routes import blueprint

# Route: Home (Book List)
@blueprint.route('/')
def index():
    books = current_app.db.bookstore.find()
    books = [
        {
            **book,
            '_id': str(book['_id']),  # Convert ObjectId to string
            'title': book.get('title', 'Untitled')  # Use 'Untitled' if title is missing
        }
        for book in books
    ]
    return render_template('home.html', books=books)


# Route: Add Book Form (GET)
@blueprint.route('/book/new', methods=['GET'])
def add_book_form():
    return render_template('add_book.html')


# Route: Add New Book (POST)
@blueprint.route('/book', methods=['POST'])
def add_book():
    new_book = {
        'title': request.form.get('title'),
        'isbn': request.form.get('isbn'),
        'year': request.form.get('year'),
        'price': request.form.get('price'),
        'page': request.form.get('page'),
        'category': request.form.get('category'),
        'publisher': {
            'id': request.form.get('publisherId'),
            'name': request.form.get('publisherName')
        },
        'author': {
            'identityNo': request.form.get('authorIdentityNo'),
            'firstName': request.form.get('authorFirstName'),
            'lastName': request.form.get('authorLastName'),
        },
    }

    # Insert new book
    current_app.db.bookstore.insert_one(new_book)
    return redirect(url_for('main.index'))


# Route: Manage Book (GET/DELETE/PUT)
@blueprint.route('/book/<id>', methods=['GET', 'DELETE', 'PUT'])
def manage_book(id):
    if request.method == 'GET':
        book = current_app.db.bookstore.find_one({"_id": ObjectId(id)})
        if book:
            book['_id'] = str(book['_id'])  # Convert ObjectId to string
            return render_template('book_details.html', book=book)
        return "Book not found", 404

    elif request.method == 'DELETE':
        result = current_app.db.bookstore.delete_one({"_id": ObjectId(id)})
        return jsonify({"success": result.deleted_count > 0})

    elif request.method == 'PUT':
        updated_data = request.json
        result = current_app.db.bookstore.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return jsonify({"success": result.matched_count > 0})


# Route: Edit Book (GET/POST)
@blueprint.route('/book/<id>/edit', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == 'GET':
        book = current_app.db.bookstore.find_one({"_id": ObjectId(id)})
        if book:
            book['_id'] = str(book['_id'])
            return render_template('edit_book.html', book=book)
        return "Book not found", 404

    # Update Book
    updated_data = {
        "title": request.form.get("title"),
        "isbn": request.form.get("isbn"),
        "year": request.form.get("year"),
        "price": request.form.get("price"),
        "page": request.form.get("page"),
        "category": request.form.get("category"),
        "publisher": {
            "id": request.form.get("publisherId"),
            "name": request.form.get("publisherName")
        },
        "author": {
            "identityNo": request.form.get("authorIdentityNo"),
            "firstName": request.form.get("authorFirstName"),
            "lastName": request.form.get("authorLastName"),
        },
    }

    result = current_app.db.bookstore.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

    if result.matched_count > 0:
        return redirect(url_for('main.index'))
    else:
        return "Error updating book", 500


# Route: Search Books
@blueprint.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')
    filter_by = request.args.get('filter', 'title')

    # Search Query
    search_query = {filter_by: {"$regex": query, "$options": "i"}} if query else {}

    books = list(current_app.db.bookstore.find(search_query))
    for book in books:
        book['_id'] = str(book['_id'])  # Convert ObjectId to string
    return render_template('home.html', books=books, query=query, filter_by=filter_by)