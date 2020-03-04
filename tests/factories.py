import factory

from factory.alchemy import SQLAlchemyModelFactory

from app.database import db
from app.models import Author, Post


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class AuthorFactory(BaseFactory):
    class Meta:
        model = Author

    username = factory.Faker('user_name')



class PostFactory(BaseFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(AuthorFactory)
    body = factory.Faker('text')
