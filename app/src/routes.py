from flask import Blueprint, jsonify
from src.models import User
from src.database import db

bp = Blueprint("api", __name__)

@bp.get("/health")
def health():
    return {"status": "ok"}, 200

@bp.get("/users")
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@bp.post("/users")
def create_user():
    user = User(name="Example User")
    db.session.add(user)
    db.session.commit()
    return {"id": user.id, "name": user.name}, 201

@bp.get("/")
def index():
    return {"message": "DevOps Projekt API dziala"}, 200