# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create DB object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration settings
    app.config['SECRET_KEY'] = 'your-secret-key'  # fixed typo
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database with the app
    db.init_app(app)  # use standard method
    # db.__init__(app)


    # Import and register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp  

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app


