from flask import Flask
from src.config import Config
from src.database import db
from src.routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(bp)
    return app
