import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@db:5432/devops_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
