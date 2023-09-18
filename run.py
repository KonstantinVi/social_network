#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask application run"""

# Python 3.11.4

# Copyright (C) 2023 "LOGO Social Network"
# This file is part of "LOGO Social Network"
# See LICENSE file for licensing information.

# Запуск приложения

# Создаёт, и записывает в окружение SECRET_KEY
# Подгрузка SECRET_KEY прописана в app/config_app.py
import starter.my_key
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
