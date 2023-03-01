from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv as env
from dotenv import load_dotenv, find_dotenv
#load variables from dotenv to variable environment
load_dotenv(find_dotenv())
app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy()

def create_app():

    app.config['SECRET_KEY'] = env('FLASK_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)

    # from .views import views
    # from .auth import auth

    #app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')
    from pyfiles.api import apipage
    app.register_blueprint(apipage, url_prefix='/api')

    return app
