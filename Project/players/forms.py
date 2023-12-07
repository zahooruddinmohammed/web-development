from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators, SubmitField

class PlayerSearchForm(FlaskForm):
    #symbol = StringField('Symbol', [validators.Length(min=1, max=10)])
    plrN = StringField('Player Name', [validators.Length(min=1, max=255)])
    submit = SubmitField("Search")
def no_numbers_in_team_name(form, field):
    if any(char.isdigit() for char in field.data):
        raise validators.ValidationError('Team name cannot contain numbers.')

class PlayerForm(FlaskForm):
    player_id = StringField('Player ID', [validators.Length(min=1, max=255)])
    name = StringField('Player Name', [validators.Length(min=1, max=255)])
    team_name = StringField('Team Name', [validators.Length(min=1, max=255), no_numbers_in_team_name])
    face_image_id = StringField('Face Image ID', [validators.Length(min=1, max=255)])
    submit = SubmitField("Save")