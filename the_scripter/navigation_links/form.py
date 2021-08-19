"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import URL, DataRequired


class RecordForm(FlaskForm):
    """
    RecordForm Class method to create a record form .
    """
    name = StringField("Name", [DataRequired()],
                       description='Name of your navigation link')
    link = StringField("Link", [DataRequired()],
                       description="accepts partial or full URL (/home or http://example.com)")
    icon = StringField("icon",
                       description='Bootstrap icon class (eg: "bi bi-alarm")')

    submit = SubmitField("Submit")
