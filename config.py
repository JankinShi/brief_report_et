# -*- coding:UTF-8 -*-
import os
import redis

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # DEBUG = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://sa:biadmin@123@172.17.1.233/HOSPITAL_CUBEDB_BQL?driver=SQL+Server+Native+Client+10.0"
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://sa:7889@localhost\MSSQLSERVER2012/HOSPITAL_CUBEDB?driver=SQL+Server+Native+Client+10.0"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # rds = redis.Redis(host='49.234.72.130', port=6379)  # redis default port

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://sa:7889@localhost/TEST?driver=SQL+Server+Native+Client+10.0"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 项目现场环境数据库配置
class ProductionConfig(Config):
    """
    sqlserver 数据库连接配置，配置格式如下：
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://用户名:密码@ip地址\实例名/数据库名?driver=SQL+Server+Native+Client+10.0"
    """
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://sa:biadmin@123@172.17.1.233/HOSPITAL_CUBEDB_BQL?driver=SQL+Server+Native+Client+10.0"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # oracle 数据库连接配置，配置格式如下


config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
