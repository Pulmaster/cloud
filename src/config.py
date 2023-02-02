from decouple import config

class Config:
    SECRET_KEY = 'P@55W6RD'
    WTF_CSRF_ENABLED = False

class DevelopmentConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig
}