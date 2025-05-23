from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
DB_NAME='database.sqlite3'

def create_database():
    db.create_all()
    print('Database created')


def create_app() :
    app=Flask(__name__)
    app.config["SECRET_KEY"]="KDK WED JKEJFKEJF"
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .admin import admin
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(admin, url_prefix='/')


    with app.app_context():
        create_database()

    return  app
