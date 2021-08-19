"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField,
    MultipleFileField
)
from wtforms.validators import URL, DataRequired, Length


class RecordForm(FlaskForm):
    """
    RecordForm Class method to create a record form .
    """
    name = StringField("Name", [DataRequired()],
                       description='Name of your script')
    description = TextAreaField("Description", [
            DataRequired(), Length(min=4, max=1024,
                                   message="Your message is too short.")
        ], description='Describe your script purpose, conditions, and risks'
    )
    link = StringField("Website", validators=[URL()],
                       description="Use full URL: (http://example.com)")
    prefix = StringField("Prefix", [DataRequired()],
                         description='Used to identify the variables in\
                              the script')
    attachments = MultipleFileField('Upload files',
                                    validators={DataRequired()},
                                    description='.SQL files only')

    submit = SubmitField("Submit")


def Form(dictionary):
    class FormGenerator(FlaskForm):
        submit = SubmitField('submit')

    for k, v in dictionary.items():
        setattr(FormGenerator, k, StringField(v, [DataRequired()]))

    return FormGenerator()

