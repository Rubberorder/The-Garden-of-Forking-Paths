# -*- coding:utf-8 -*-
#encoding = utf-8
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:7123@localhost:3306/flask_database?charset=utf8'
    POSTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass

config = Config()


# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#         'mysql+pymysql://root:7123@localhost:3306/dev_database'


# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
#         'mysql+pymysql://root:7123@localhost:3306/test_database'

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'mysql+pymysql://root:7123@localhost:3306/database'

# config = {
#     'development': DevelopmentConfig,
#     'testing': TestingConfig,
#     'production': ProductionConfig,
#     'default': DevelopmentConfig
# }
