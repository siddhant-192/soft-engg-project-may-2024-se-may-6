import os

baseDir = os.path.abspath(os.path.dirname(__file__))
class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = "redis://127.0.0.1:6379/1"
    CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"
    CELERY_TIMEZONE = "Asia/Kolkata"
    REDIS_URL = "redis://127.0.0.1:6379"
    CACHE_TYPE="RedisCache"
    CACHE_REDIS_HOST="127.0.0.1"
    CACHE_REDIS_PORT=6379

class LocalDevConfig(Config):
    SQLITE_DB_DIR = os.path.join(baseDir, "../data")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, 'data.sqlite3')
    DEBUG = True
    REDIS_URL = "redis://127.0.0.1:6379"

class ProductionConfig(Config):
    user = 'lmsApp'
    password = 'lmsApp@123'
    host = 'localhost'
    port = 5432
    database = 'LMS-DB'
    SQLALCHEMY_DATABASE_URI = ('postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, database))
    DEBUG = False