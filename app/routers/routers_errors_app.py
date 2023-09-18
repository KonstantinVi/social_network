#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Модуль Маршрутов ошибок Запроса и Ответа:\n
    4xx - Client Errors
    --------------------------------
    + **400** - Bad Request
    + **401** - Unauthorized
    + **403** - Forbidden
    + **404** - Not Found
    + **405** - Method Not Allowed
    + **408** - Request Timeout
    + **429** - Too many Requests

    5xx - Server Errors
    --------------------------------
    + **500** - Internal Server Error
    + **501** - Not Implemented
    + **502** - Bad Gateway
    + **503** - Service Unavailable
    + **504** - Gateway Timeout
    + **505** - HTTP Version Not Supported
"""

# Copyright (C) 2023 "LOGO Social Network"
# This file is part of "LOGO Social Network"
# See LICENSE file for licensing information.


# Стандартные библиотека Python

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


moment = Moment(app)


# ------ 4xx - Client Errors ------
@app.errorhandler(400)
def error(e):
    """400 - Bad Request"""
    return ..., 400


@app.errorhandler(401)
def error(e):
    """401 - Unauthorized"""
    return ..., 401


@app.errorhandler(403)
def error(e):
    """403 - Forbidden"""
    return ..., 403


@app.errorhandler(404)
def error(e):
    """404 Not Found"""
    return render_template('errors/404.html'), 404


@app.errorhandler(405)
def error(e):
    """405 - Method Not Allowed"""
    return ..., 405


@app.errorhandler(408)
def error(e):
    """408 - Request Timeout"""
    return ..., 408


@app.errorhandler(429)
def error(e):
    """429 - Too many Requests"""
    return ..., 429


# ------ 5xx - Server Errors ------
@app.errorhandler(500)
def error(e):
    """500 - Internal Server Error"""
    return render_template('errors/500.html'), 500


@app.errorhandler(501)
def error(e):
    """501 - Not Implemented"""
    return ..., 501


@app.errorhandler(502)
def error(e):
    """502 - Bad Gateway"""
    return ..., 502


@app.errorhandler(503)
def error(e):
    """503 - Service Unavailable"""
    return ..., 503


@app.errorhandler(504)
def error(e):
    """504 - Gateway Timeout"""
    return ..., 504


@app.errorhandler(505)
def error(e):
    """505 - HTTP Version Not Supported"""
    return ..., 505
