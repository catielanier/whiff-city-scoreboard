import jwt
from flask import Blueprint, request, jsonify, Response
from gotrue import AuthResponse
from supabase import Client

from utils.supabase_client import get_client
from utils.constants import SECRET

supabase: Client = get_client()

user_routes: Blueprint = Blueprint("user_routes", __name__)


def generate_token(user: AuthResponse) -> str:
    token: str = jwt.encode({"user": user}, SECRET, algorithm="HS256")
    return token

@user_routes.route("/login", methods=["POST"])
def login() -> Response:
    post_data = request.get_json()
    email: str = post_data.get("email")
    password: str = post_data.get("password")
    res: AuthResponse = supabase.auth.sign_in_with_password({
        "email": email, "password": password
    })
    if res.user.role == "authenticated":
        token: str = generate_token(res)
        return jsonify({
            "status": 201,
            "message": "Successfully logged in",
            "token": token
        })
    return jsonify({
        "status": 401,
        "message": "Invalid email or password"
    })