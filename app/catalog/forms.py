from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = StringField('Number of Pages', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Update Book Detail')

class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    avg_rating = StringField('Average rating', validators=[DataRequired(), Length(1, 5, 'Rating is must be out of five(1.0-5.0)')])
    format = StringField('Format', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired()])
    num_pages = StringField('Number of Pages', validators=[DataRequired()])
    pub_id = StringField("Publisher Id", validators=[DataRequired()])

    submit = SubmitField('Add Book Detail')

