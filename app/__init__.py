#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python 3.11.4

# Copyright (C) 2023 "LOGO Social Network"
# This file is part of "LOGO Social Network"
# See LICENSE file for licensing information.

# Стандартные библиотека Python.
import os

# Сторонние библиотеки Python.
from flask import Flask

# Импорт конфигурации Приложения.
from app.config_app import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app_env = os.environ.get('FLASK_ENV', 'default')

    # Режим "Разработки".
    if app_env == 'development':
        app.config.from_object('app.config.DevelopmentConfig')

        # Дебаг панель - настройка.
        app.debug = True
        # Дебаг панель - ВКЛ / ВЫКЛ.
        toolbar = DebugToolbarExtension(app)

    # Режим "Тестирования".
    elif app_env == 'testing':
        app.config.from_object('app.config.TestingConfig')

    # Режим "Работы".
    else:
        app.config.from_object('app.config.Config')


    # Инициализация других компонентов
    # Инициализация Database
    db.init_app(app)

    # Подключение api.
    # api version 1.
    from app.api.v1.open_api import open_api_v1
    from app.api.v1.partner_api import partner_api_v1
    from app.api.v1.private_api import private_api_v1

    # api version 1.
    app.register_blueprint(open_api_v1, url_prefix='/api/v1/open')
    app.register_blueprint(partner_api_v1, url_prefix='/api/v1/partner')
    app.register_blueprint(private_api_v1, url_prefix='/api/v1/private')

    return app


# from app import routers
#
# from app.blueprints.auth import bp as auth_bp
# from app.blueprints.main import bp as main_bp
#
# app.register_blueprint(auth_bp)
# app.register_blueprint(main_bp)
