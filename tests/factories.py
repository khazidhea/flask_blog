import factory

from factory.alchemy import SQLAlchemyModelFactory

from app.database import db
from app.models import Author


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class AuthorFactory(BaseFactory):
    username = factory.Faker('user_name')

    class Meta:
        model = Author
