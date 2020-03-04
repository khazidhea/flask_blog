from app.models import Author


def test_author(db):
    author = Author(username='author')
    db.session.add(author)
    db.session.commit()
    assert Author.query.first().username == 'author'
