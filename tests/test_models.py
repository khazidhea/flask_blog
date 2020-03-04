from app.models import Author

from .factories import AuthorFactory


def test_author(db):
    author = AuthorFactory()
    assert Author.query.first().username
