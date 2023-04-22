from flask_wtf import FlaskForm
import wtforms


class AddFilmForm(FlaskForm):
    title = wtforms.StringField('Title', validators=[wtforms.validators.DataRequired()])
    release = wtforms.StringField('Release', validators=[wtforms.validators.DataRequired()])
    created_in_country = wtforms.StringField('Created_in_country', validators=[wtforms.validators.DataRequired()])
    available_in_countries = wtforms.StringField('Available_in_countries', validators=[wtforms.validators.DataRequired()])
    category = wtforms.StringField('Category', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Submit')

class AddDirectorForm(FlaskForm):
    first_name = wtforms.StringField('First_name', validators=[wtforms.validators.DataRequired()])
    last_name = wtforms.StringField('Last_name', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Submit')
