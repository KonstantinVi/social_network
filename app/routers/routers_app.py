#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Модуль Маршрутов end-point app.\n
    + '/' - index()
"""

# Copyright (C) 2023 "LOGO Social Network"
# This file is part of "LOGO Social Network"
# See LICENSE file for licensing information.


# Стандартные библиотека Python
import logging

# Сторонние библиотеки Python
# Application Context | current_app | g
from flask import current_app
from flask import g
# Request Context | request | session
from flask import request
from flask import session
# ------------------------------------------
from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from flask import make_response
from flask_moment import Moment

# Библиотеки Проекта
from app import app
from app.forms.forms_reg_log import LogiInForm
from app.forms.forms_reg_log import PasswordRecovery
from app.forms.forms_reg_log import RegistrationForm
from app.forms.forms_of_platform_interaction import FeedbackForm
import logs.log_config as log_config


# Логирование | Настройка лежит logs/log_config.py
log_config.setup_logging()
logger = logging.getLogger(__name__)


moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html'), 200


@app.route('/page')
def page_():
    # print(request.cookies['name'])
    reload_cookie = False  # Тумблер для перзагрузки cookie
    list_name_cookies = ('name', 'favorite-font', 'favorite-color')
    if any(map(lambda x: x not in request.cookies.keys(),
               list_name_cookies)) or reload_cookie:
        my_response = make_response(
            render_template('page.html', status_cookie='cookie reload!'), 200)
        my_response.set_cookie("favorite-color",
                               "skyblue",
                               60 * 60 * 24 * 15,
                               samesite=None,
                               httponly=True)
        my_response.set_cookie("favorite-font",
                               "sans-serif",
                               60 * 60 * 24 * 15,
                               samesite=None,
                               httponly=True)
        my_response.set_cookie("name",
                               "Konstantin",
                               60 * 60 * 24 * 15,
                               httponly=True)
        logger.info('cookie установлены!')
    else:
        my_response = make_response(
            render_template('page.html', status_cookie='cookie ok!'), 200)
        logger.info('cookie уже есть!')
    return my_response


# - block start ----------- login | registration -----------


@app.route('/login', methods=['GET', 'POST'])
def login_():
    """Форма Входа в систему"""
    form = LogiInForm()
    tmp_url = (url_for('registration_'))
    if form.validate_on_submit():
        flash('Данные введены верно', 'success')
        logger.info(f'{form.user_login.data} осуществил Вход - Успех!')
    return render_template('reg_log/login.html', form=form,
                           tmp_url=tmp_url), 200


@app.route('/recpass', methods=['GET', 'POST'])
def pass_recovery_():
    """Форма восстановления пароля"""
    form = PasswordRecovery()
    if form.validate_on_submit():
        flash('Новый пароль выслан на ваш e-mail', 'success')
        logger.info('Восстановление пароля - Успех!')
        return redirect(url_for('login_')), 302
    return render_template('reg_log/pass_recovery.html', form=form), 200


@app.route('/registration', methods=['GET', 'POST'])
def registration_():
    """Форма регистрации"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Регистрация прошла успено', 'success')
        logger.info('Регистрация - Успех!')
        return redirect(url_for('login_')), 302
    return render_template('reg_log/registration.html', form=form), 200


# - block end ----------- login | registration -----------


@app.route('/feedback', methods=['GET', 'POST'])
def feedback_():
    """Форма обратной связи"""
    form = FeedbackForm()
    if form.validate_on_submit():
        flash('Сообщение отправлено', 'success')
        logger.info('Сообщение отправлено - Успех!')
        return redirect(url_for('feedback_')), 302
    return render_template('feedback.html', form=form), 200
