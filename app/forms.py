from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField, IntegerField, SelectField, FileField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Regexp, InputRequired
import re, os
from flask import request
from flask_wtf.csrf import CSRFProtect

class PropertyForm(FlaskForm):
    propertyTitle = StringField("Property Title", validators=[InputRequired()])

    description = TextAreaField("Description", validators=[InputRequired()])

    numBedrooms = StringField("No. of Rooms", validators=[InputRequired()])

    numBathrooms = StringField("No. of Bathrooms", validators=[InputRequired()])

    price = StringField("Price", validators=[InputRequired()])

    types = SelectField("Property Type", choices=["House", 'Appartment'], validators=[InputRequired()])  # Ensure to populate choices

    location = StringField("Location", validators=[InputRequired()])

    photo = FileField('Image File',
        validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')]

        )





