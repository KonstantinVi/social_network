from flask import Blueprint, render_template, redirect, url_for
from app.forms import LoginForm

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login user
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)
