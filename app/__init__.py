from flask import Flask

from . import models
from .config import Config
from .database import db, migrate


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_shellcontext(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_shellcontext(app):
    def shell_context():
        context = {'db': db}
        models = [
            cls for cls in db.Model._decl_class_registry.values()
            if isinstance(cls, type) and issubclass(cls, db.Model)
        ]
        context.update({model.__name__: model for model in models})
        return context

    app.shell_context_processor(shell_context)


app = create_app()
