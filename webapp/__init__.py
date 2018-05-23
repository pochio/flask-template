# app/__init__.py

from flask import Flask, redirect

from config import app_config

def create_app(config_name):

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')

    @app.route('/')
    def root_redirect():
        return redirect('/helloworld/')

    from .admin import app as admin
    app.register_blueprint(admin)

    from .helloworld.views import helloworld
    app.register_blueprint(helloworld)

    return app

