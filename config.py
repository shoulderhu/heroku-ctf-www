import os


class Config:
    SECRET_KEY = os.urandom(16)
    JSON_SORT_KEYS = False

    #SSL
    SSL_REDIRECT = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class ProductionConfig(Config):
    SSL_REDIRECT = True


class HerokuConfig(ProductionConfig):
    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "heroku": HerokuConfig,
    "default": DevelopmentConfig
}
