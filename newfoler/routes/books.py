# from flask import  request, jsonify, Blueprint
# from middleware.auth import authenticate_token
# todos_bp= Blueprint("todos",__name__)

# todos=[]

# @todos_bp.before_request
# def before_request():
#     authenticate_token()

# @todos_bp.route("/", methods=["GET"])
# def get_todos():
#     return jsonify(todos)

# @todos_bp.route("/", methods=["POST"])
# def create_todos():
#     todo={
#         "id": len(todos)+1,
#         "title": request.json.get("title"),
#         "completed": request.json.get("completed",False),
#     }    
#     todos.append(todo)
#     return jsonify(todo),201


# @todos_bp.route("/<int:id>",methods=["PUT"])
# def update_todo(id):
#     todo = next((t for t in todos if t["id"]==id),None)
#     if todo is None:
#         return jsonify({"error": "Todo not found"}),404
#     todo["title"]=request.json.get("title",todo["title"])
#     todo["completed"]=request.json.get("completed",todo["completed"])
#     return jsonify(todo)    


# @todos_bp.route("/<int:id>",methods=["DELETE"])
# def delete_todo(id):
#     global todos
#     todos = [t for t in todos if t["id"]!=id]
#     return '',204


from flask import Blueprint, request, jsonify

books_bp = Blueprint("books", __name__)


books = []
    

@books_bp.before_request
def before_request():
    authenticate_token()

@books_bp.route("/", methods=["GET"])
def get_books():
    return jsonify(books)

# Get a single book by ID
@books_bp.route("/<int:id>", methods=["GET"])
def get_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

# Create a new book
@books_bp.route("/", methods=["POST"])
def create_book():
    new_book = {
        "id": len(books) + 1,
        "title": request.json.get("title"),
        "author": request.json.get("author"),
        "available": request.json.get("available", True)
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book by ID
@books_bp.route("/<int:id>", methods=["PUT"])
def update_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    book["title"] = request.json.get("title", book["title"])
    book["author"] = request.json.get("author", book["author"])
    book["available"] = request.json.get("available", book["available"])
    return jsonify(book)

# Delete a book by ID
@books_bp.route("/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]
    return '', 204

   