"""Классы форм связанных с платформой:\n
class FeedbackForm() - Класс формы обратной связи\n
"""
from flask_wtf import FlaskForm
# Поля формы
from wtforms import StringField
from wtforms import SubmitField
from wtforms import EmailField
from wtforms import TextAreaField
# Валидаторы полей формы
from wtforms.validators import InputRequired  # Не пустое поле
from wtforms.validators import Email


class FeedbackForm(FlaskForm):
    """Класс формы обратной связи
    Attributes:
        user_first_name
        user_last_name
        user_login
        user_message
        submit_int
    """
    user_first_name = StringField('Ваше Имя',
                                  validators=[InputRequired()])
    user_last_name = StringField('Ваша Фамилия',
                                 validators=[InputRequired()])
    user_login = EmailField('Ваш e-mail',
                            validators=[InputRequired(), Email("Ошибка! Некорректный е-mail адрес")])
    user_message = TextAreaField('Ваше сообщение',
                            validators=[InputRequired()])
    submit_int = SubmitField('Отправить')
