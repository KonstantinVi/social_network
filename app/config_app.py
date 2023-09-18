"""Конфигурация Flask приложения"""
import datetime
import os
import starter.__vhjvmdfgoj as vhj

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """'Базовый Класс' конфигурации приложения.\n
    :argument
        + SECRET_KEY
        + DEBUG - False
        + TESTING - False
        SQLALchemy
            + SQLALCHEMY_DATABASE_URI
            + SQLALCHEMY_TRACK_MODIFICATIONS = False
            + SQLALCHEMY_COMMIT_ON_TEARDOWN = True
        + PERMANENT_SESSION_LIFETIME - days=15
        + Flask-Mail
        + Flask_WTF
        """
    # Секретный Ключ.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'whrt8424tgwtj43294982turgyjwyvhvkjdhtk')

    # Режим разработки.
    DEBUG = False
    TESTING = False

    # DB
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Время сохранения session на стороне Клиента.
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=15)


#     # Настройка Flask-Mail
#     FLASK_MAIL_SERVER = 'smtp.googlemail.com'
#     FLASK_MAIL_PORT = 587
#     FLASK_MAIL_USE_TLS = True
#     FLASK_MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME') or 'YOU_MAIL@gmail.com'
    FLASK_MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD') or 'vhj.flask_mail_password'
#     FLASK_MAIL_DEFAULT_SENDER = MAIL_USERNAME

#     ##### WTF_FORM #####
#     CSRF_ENABLED = True
#     WTF_CSRF_SECRET_KEY = SECRET_KEY


class DevelopmentConfig(BaseConfig):
    """Класс 'Разработка', наследуется от 'Базового Класса' конфигурации.\n
    :argument
        + DEBUG - True"""
    # Режим разработки.
    DEBUG = True
#     ASSETS_DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') \
#                           or 'mysql+pymysql://root:pass@localhost/flask_app_db'


class ProductionConfig(BaseConfig):
    # Режим разработки.
    DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')\
#                           or 'mysql+pymysql://root:pass@localhost/flask_app_db'


class TestingConfig(BaseConfig):
    """Класс 'Тестирование', наследуется от 'Базового Класса' конфигурации.\n
       :argument
           + DEBUG - True
           + TESTING - True
           + SQLALCHEMY_DATABASE_URI"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'





# basedir = os.path.abspath(os.path.dirname(__file__))


# ------------------------ КОНФИГУРАЦИЯ ----------------------------
# Режим разработки.
# DEBUG = True
# Секретный Ключ.
# SECRET_KEY = os.environ.get('SECRET_KEY')
# Время сохранения session на стороне Клиента.
# PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=15)
# SQLAlchemy DB
# SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True


# if 'SECRET_KEY' in os.environ:
#     print(' * SECRET_KEY - Установлен в окружение!')

#
# class BaseConfig:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
#     FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
#
#     # DB
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#     SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://webuser:web_password@localhost/webuser_db'
#
#     ##### настройка Flask-Mail #####
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'YOU_MAIL@gmail.com'
#     MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
#     MAIL_DEFAULT_SENDER = MAIL_USERNAME
#
#     ##### WTF_FORM #####
#     CSRF_ENABLED = True
#     WTF_CSRF_SECRET_KEY = 'dsofpkoasodksap'
#
#
# class DevelopementConfig(BaseConfig):
#     DEBUG = True
#     ASSETS_DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') \
#                           or 'mysql+pymysql://root:pass@localhost/flask_app_db'
#
#
# class TestingConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI')\
#                               or 'mysql+pymysql://root:pass@localhost/flask_app_db'
#
#
# class ProductionConfig(BaseConfig):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')\
#                           or 'mysql+pymysql://root:pass@localhost/flask_app_db'
