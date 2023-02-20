from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy()

def create_app():

    app.config['SECRET_KEY'] = 'asdflwefDKLFJSWFSDFLWiov'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:OneTwoPost123@192.168.1.11:5432/supersms-test'
    db.init_app(app)

    # from .views import views
    # from .auth import auth

    #app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')
    from pyfiles.api import apipage
    app.register_blueprint(apipage, url_prefix='/api')

    return app
