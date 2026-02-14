import pytest

from src.infra.db import db
from app import create_app

@pytest.fixture
def session():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()
        yield db.session
        db.session.rollback()
        db.drop_all()

@pytest.fixture
def client():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()
        with app.test_client() as client:
            yield client
        db.drop_all()