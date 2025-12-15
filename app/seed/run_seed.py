from src import create_app
from src.database import db
from src.models import User
import os

app = create_app()

with app.app_context():
    db.create_all()

    if not User.query.first():
        user = User(name="Seed User")
        db.session.add(user)
        db.session.commit()

    os.makedirs("/seed_output", exist_ok=True)
    with open("/seed_output/report.txt", "w") as f:
        f.write("Seeding completed successfully\n")
