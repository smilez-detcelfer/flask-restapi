from flask import Flask
from os import getenv as env
from src.models import db
from dotenv import load_dotenv, find_dotenv
from flask_apscheduler import APScheduler

#load variables from dotenv to variable environment
load_dotenv(find_dotenv())
app = Flask(__name__, instance_relative_config=True)
scheduler = APScheduler()


def create_app():

    app.config['SECRET_KEY'] = env('FLASK_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    scheduler.init_app(app)
    scheduler.start()
    from src.api import apipage
    app.register_blueprint(apipage, url_prefix='/api')

    return app
