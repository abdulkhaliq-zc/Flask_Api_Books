from flask import  request, jsonify

Token= "mysecrettoken"

def authenticate_token():
    token= request.headers.get("Authorization")
    if not token or token != f"Bearer {Token}":
        return jsonify({"error": "Unauthorized"}),401