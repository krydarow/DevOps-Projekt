from src import create_app
from src.database import db
from src.models import User

import os
import csv
import json
import logging

OUTPUT_DIR = "/seed_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(OUTPUT_DIR, "seed.log"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = create_app()

with app.app_context():
    db.create_all()

    if not User.query.first():
        users = [
            User(name="Kamil"),
            User(name="Robert"),
            User(name="Kacper"),
            User(name="Mateusz"),
            User(name="Wojtek"),
        ]

        db.session.add_all(users)
        db.session.commit()
        logging.info("Inserted 5 users")

    users = User.query.all()

    with open(os.path.join(OUTPUT_DIR, "users.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name"])
        for u in users:
            writer.writerow([u.id, u.name])

    with open(os.path.join(OUTPUT_DIR, "data.json"), "w") as f:
        json.dump(
            [{"id": u.id, "name": u.name} for u in users],
            f,
            indent=2
        )


    logging.info("Seeder finished successfully")
