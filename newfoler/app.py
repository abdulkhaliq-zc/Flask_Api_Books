
# from flask import Flask, request, render_template
# from routes.test import todos_bp

# app = Flask(__name__)
# app.register_blueprint(todos_bp,url_prefix="/todos")


# @app.errorhandler(404)
# def not_found (e):
#     return jsonify({"error":"Resource not found"}), 404
# if __name__ == '__main__':
#     app.run(port=3000)

from flask import Flask, jsonify
from routes.books import books_bp

app = Flask(__name__)
app.register_blueprint(books_bp, url_prefix="/books")

# Error handling
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(port=3000)

