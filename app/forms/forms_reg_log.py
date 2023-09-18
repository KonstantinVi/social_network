"""Классы форм связанных с регистрацией и аутентификацией:\n
class LogiInForm() - Класс формы аутентификации\n
class PasswordRecovery() - Класс восстановления пароля\n
class RegistrationForm() - Класс формы регистрации\n
"""
from flask_wtf import FlaskForm
# Поля формы
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import EmailField
# Валидаторы полей формы
from wtforms.validators import InputRequired  # Не пустое поле
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length


class LogiInForm(FlaskForm):
    """Класс формы аутентификации
    Attributes:
        user_login
        user_pass
        submit_log
        user_save
    """
    user_login = EmailField('Username',
                            validators=[InputRequired(), Email("Ошибка! Некорректный е-mail адрес")])
    user_pass = PasswordField('Password',
                              validators=[InputRequired(), Length(min=10, max=35, message="Ошибка! Пароль должен быть от 10 до 35 символов")])
    submit_log = SubmitField("Войти")
    user_save = BooleanField("Запомнить меня", default=True)


class PasswordRecovery(FlaskForm):
    """Класс формы восстановления пароля
    Attributes:
        user_login
        submit
    """
    user_login = EmailField('Username',
                            validators=[InputRequired(), Email("Ошибка! Некорректный е-mail адрес")])
    submit = SubmitField("Прислать мне новый пароль")


class RegistrationForm(FlaskForm):
    """Класс формы регистрации
    Attributes:
        user_login
        user_pass
        user_conf_pass
        user_save
        submit_reg
    """
    user_login = EmailField('Username',
                            validators=[InputRequired(), Email("Ошибка! Некорректный е-mail адрес")])
    user_pass = PasswordField('Password',
                              validators=[InputRequired(), Length(min=10, max=35, message="Ошибка! Пароль должен быть от 10 до 35 символов")])
    user_conf_pass = PasswordField('Confirm password',
                                   validators=[InputRequired(), EqualTo('user_pass', message='Ошибка! Пароли не совпадают!')])
    user_save = BooleanField("Запомнить меня", default=True)
    submit_reg = SubmitField("Регистрация")
