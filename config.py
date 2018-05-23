# config.py

class Config(object):
    FLASK_ADMIN_SWATCH = 'superhero'
    SECRET_KEY = 'SECRET_KEY'

class DevelopmentConfig(Config):

    DEBUG = True

class ProductionConfig(Config):

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

