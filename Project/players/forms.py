from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators, SubmitField

class PlayerSearchForm(FlaskForm):
    #symbol = StringField('Symbol', [validators.Length(min=1, max=10)])
    plrN = StringField('Player Name', [validators.Length(min=1, max=255)])
    submit = SubmitField("Search")

class PlayerForm(FlaskForm):
    player_id = StringField('Player ID', [validators.Length(min=1, max=255)])
    name = StringField('Player Name', [validators.Length(min=1, max=255)])
    team_name = StringField('Team Name', [validators.Length(min=1, max=255)])
    face_image_id = StringField('Face Image ID', [validators.Length(min=1, max=255)])
    submit = SubmitField("Save")