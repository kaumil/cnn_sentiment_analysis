from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class InputStringForm(FlaskForm):
    input_string = TextAreaField('Enter Input String',validators=[DataRequired(),Length(min=1,max=50000)])
    submit = SubmitField('Submit')
