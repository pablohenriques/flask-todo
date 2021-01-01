
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "VFsS3neMKuxFmrOrvaEdcA"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
