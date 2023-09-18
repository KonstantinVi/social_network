"""Создание SECRET_KEY в виртуальное окружение"""

import os


# Создание Ключа приложения.
new_key = os.urandom(50).hex()
# print(new_key)
os.environ.setdefault('SECRET_KEY', f'{new_key}')
