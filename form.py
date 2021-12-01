from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class ContectForm(FlaskForm):
    name = StringField('Email:', validators = [DataRequired(), Length(min=2, max=10)])
    submit = SubmitField('Send')