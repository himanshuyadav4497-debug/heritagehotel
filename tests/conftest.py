
import pytest

from app import create_app, db


@pytest.fixture()
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
    })

    with app.app_context():
        # Create database tables before running tests.
        db.create_all()

        with app.test_client() as client:
            yield client

        # Clean up the test database.
        db.session.remove()
        db.drop_all()
