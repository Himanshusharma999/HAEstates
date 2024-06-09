from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

#from HAEstates.queries import get_user_by_user_name, get_farmer_by_pk, get_customer_by_pk
from HAEstates.utils.choices import PropertyTypeChoices

class FilterPropertyForm(FlaskForm):
    category = SelectField('Type',
                           choices=PropertyTypeChoices.choices())
    item = IntegerField('Beds',
                       validators=[NumberRange(min=0, max=100)])
    variety = IntegerField('Baths',
                          validators=[NumberRange(min=0, max=100)])
    stories = IntegerField('Stories',
                            validators=[NumberRange(min=0, max=100)])
    sold_by = IntegerField('stories',
                          validators=[NumberRange(min=0, max=100)])
    price = FloatField('Price (lower than or equal to)',
                       validators=[NumberRange(min=0, max=100000000000)])

    submit = SubmitField('Search homes')

