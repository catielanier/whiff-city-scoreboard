from flask import Blueprint, request, jsonify, Response
from postgrest import APIResponse
from supabase import Client
from flask_socketio import emit

from utils.supabase_client import get_client

supabase: Client = get_client()

scoreboard_routes: Blueprint = Blueprint("scoreboard_routes", __name__)


@scoreboard_routes.route("/", methods=["GET"])
def get_scoreboard() -> Response:
    player_scores: APIResponse = supabase.table("player_scores").select("*").execute()
    return jsonify({
        "status": 200,
        "player_scores": player_scores.data,
    })

@scoreboard_routes.route("/", methods=["PUT"])
def update_scoreboard() -> Response:
    put_data = request.get_json()
    player_scores = put_data.get("player_scores")
    commentator_info = put_data.get("commentator_info")
    updated_scores: APIResponse = supabase.table("player_scores").update(player_scores).execute()
    updated_info: APIResponse = supabase.table("commentator_info").update(commentator_info).execute()

    emit("scoreboard_updated", {}, broadcast=True)

    return jsonify({
        "status": 201,
        "message": "Successfully updated scoreboard",
        "player_scores": updated_scores.data,
        "commentator_info": updated_info.data
    })

@scoreboard_routes.route("/new", methods=["POST"])
def create_scoreboard() -> Response:
    post_data = request.get_json()
    player_scores = post_data.get("player_scores")
    commentator_info = post_data.get("commentator_info")
    created_scores: APIResponse = supabase.table("player_scores").insert(player_scores).execute()
    created_info: APIResponse = supabase.table("commentator_info").insert(commentator_info).execute()

    return jsonify({
        "status": 201,
        "message": "Successfully created scoreboard",
        "player_scores": created_scores.data,
        "commentator_info": created_info.data
    })