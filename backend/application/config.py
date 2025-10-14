class LocalDevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///my_db.sqlite3"
    SECURITY_PASSWORD_SALT = "mysecretsalt"
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECRET_KEY = "mysecretkey"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_TOKEN_MAX_AGE = 7200  # 2 hour

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_DEFAULT_TIMEOUT = 30 
    CELERY_BROKER_URL = 'redis://localhost:6379'