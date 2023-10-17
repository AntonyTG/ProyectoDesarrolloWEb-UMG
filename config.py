class Config:
    SECRET_KEY = 'prueba'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}