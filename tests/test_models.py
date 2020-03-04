from app.models import Author, Post

from .factories import AuthorFactory, PostFactory


def test_author():
    author = AuthorFactory()
    assert Author.query.first().username


def test_post():
    posts = PostFactory.create_batch(10)
    assert Author.query.count() == 10
    assert Post.query.count() == 10
