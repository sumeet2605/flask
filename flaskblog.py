from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from image import get_images
import os
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '66c3c4b36ad416f15a6bd7b94edaf265'




posts= get_images()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for { form.username.data }!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'passwrod':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))