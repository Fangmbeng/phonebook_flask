from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import ContactForm, Signupform
from app.models import User

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        check_user = User.query.filter((email == email) | (username == username)).all
        if check_user:
            flash("This user already exist")
            return redirect(url_for("signup"))
        new_user = User(
            email = email, 
            password = password, 
            username = username)
        if new_user:
            flash(f"Thank {username}/{email} for signing up")
            return redirect(url_for('index'))
    return render_template("signup.html", form = form)

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    form = ContactForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        mobile_number = form.mobile_phone.data
        office_number = form.office_phone.data
        new_phonebook = User.phonebook(
            first_name = first_name,
            last_name = last_name,
            mobile_number = mobile_number,
            office_number = office_number
            )
        if new_phonebook:
            flash('Contact has been added')
            return redirect(url_for('index'))
    return render_template('posts.html', form = form)