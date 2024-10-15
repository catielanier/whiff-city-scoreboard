import os
import jwt
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify, Response

from server import supabase

load_dotenv()
SECRET: str = os.getenv("SECRET")

user_routes = Blueprint("user_routes", __name__)


def generate_token(user) -> str:
    token: str = jwt.encode({"user": user}, SECRET, algorithm="HS256")
    return token

@user_routes.route("/login", methods=["POST"])
def login() -> Response:
    post_data = request.get_json()
    email: str = post_data.get("email")
    password: str = post_data.get("password")
    res = supabase.auth.sign_in_with_password({
        "email": email, "password": password
    })
    if res.user.role == "authenticated":
        jwt: str = generate_token(res)
        return jsonify({
            "status": 201,
            "message": "Successfully logged in",
            "token": jwt
        })
    return jsonify({
        "status": 401,
        "message": "Invalid email or password"
    })