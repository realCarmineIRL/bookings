from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    # with app.app_context():
    #     db.create_all()  # Create sql tables for our data models
    return app


def initialize_extensions(app):

    db.init_app(app)


def register_blueprints(app):

    from project.bookings import bookings_blueprint

    app.register_blueprint(bookings_blueprint)
