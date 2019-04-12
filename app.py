from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # Initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    # import blueprints
    from contact import bp_contact

    # register blueprint
    app.register_blueprint(bp_contact)


    return app

