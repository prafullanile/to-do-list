from flask import Flask, flash, redirect, render_template, request, url_for, session, Blueprint

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'prafull',
    'password': '0318'
}


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash('Login successful', 'success')
            return redirect(url_for('auth.login'))  # Optional: redirect after login
        else:
            flash('Invalid username or password', 'danger')

    return render_template("login.html")

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out', 'info')
    return redirect(url_for('auth.login'))


