from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from . import todo
from . import auth

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///todoList.db'
        # SQLALCHEMY_DATABASE_URI='postgresql+psycopg://cursos:cursos1234@localhost/cursos'
    )
    
    db.init_app(app)

    # register blueprint

    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route("/")
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()

    return app
