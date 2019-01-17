import os

class Config:
    """Parent configuration class."""
    DEBUG = False
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DB_USER = 'bochie'
    DB_PASSWORD = 'jamohsize'
    DB_HOST = '127.0.0.1'
    DB_PORT = '5432'
    DB_NAME = 'questioner'


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    DB_USER = 'bochie'
    DB_PASSWORD = 'jamohsize'
    DB_HOST = '127.0.0.1'
    DB_PORT = '5432'
    DB_NAME = 'questioner_test'


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
