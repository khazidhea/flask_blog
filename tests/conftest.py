import pytest

from app import create_app
from app.config import TestConfig
from app.database import db as _db


@pytest.fixture
def app():
    app = create_app(config=TestConfig)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.yield_fixture
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()
