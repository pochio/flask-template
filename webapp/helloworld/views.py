# sample/helloworld.py

from flask import Blueprint

helloworld = Blueprint('helloworld', __name__, url_prefix='/helloworld')

@helloworld.route('/')
def helloworld_root():
    return 'Hello World!'

