from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    WTF_CSRF_ENABLED = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}