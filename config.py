__author__ = 'trust'

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\x84\x0b\xa3\xda\xb0\xe1\x1a\x7f9\x13\xdf\xdd\xd9\xbc\xe7\xee\xfdBy\xae\xfcA6\xa6'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
