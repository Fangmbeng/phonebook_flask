from flask_wtf import FlaskForm, Form
from wtforms import StringField, IntegerField, EmailField, PasswordField, SubmitField, FormField
from wtforms.validators import DataRequired, EqualTo, InputRequired

class Signupform(FlaskForm):
    email = EmailField('Email', validators = [InputRequired()])
    username = StringField('username', validators = [InputRequired()])
    password = PasswordField('password', validators = [InputRequired()])
    confirm_password = PasswordField('confirm password', validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField()

class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code', validators = [InputRequired()])
    area_code    = IntegerField('Area Code/Exchange', validators = [InputRequired()])
    number       = StringField('Number', validators = [InputRequired()])

class ContactForm(FlaskForm):
    first_name   = StringField('First name', validators = [InputRequired()])
    last_name    = StringField('last name', validators = [InputRequired()])
    mobile_phone = FormField(TelephoneForm)
    office_phone = FormField(TelephoneForm)
    submit = SubmitField()
