from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators, SubmitField

class PlayerSearchForm(FlaskForm):
    #symbol = StringField('Symbol', [validators.Length(min=1, max=10)])
    plrN = StringField('Player Name', [validators.Length(min=1, max=255)])
   
def no_numbers_in_team_name(form, field):
    if any(char.isdigit() for char in field.data):
        raise validators.ValidationError('Team name cannot contain numbers.')

class PlayerForm(FlaskForm):
    player_id = StringField('Player ID', [
        validators.Length(min=1, max=255, message='Player ID must be between 1 and 255 characters'),
        validators.Regexp('^[A-Za-z0-9_-]+$', message='Player ID can only contain letters, numbers, underscores, and hyphens')
    ])
    
    name = StringField('Player Name', [
        validators.Length(min=1, max=255, message='Player Name must be between 1 and 255 characters')
    ])
    
    team_name = StringField('Team Name', [
        validators.Length(min=1, max=255, message='Team Name must be between 1 and 255 characters'),
        validators.Regexp('^[A-Za-z0-9_-]+$', message='Team Name can only contain letters, numbers, underscores, and hyphens')
    ])
    
    face_image_id = StringField('Face Image ID', [
        validators.Length(min=1, max=255, message='Face Image ID must be between 1 and 255 characters'),
        validators.Regexp('^[A-Za-z0-9_-]+$', message='Face Image ID can only contain letters, numbers, underscores, and hyphens')
    ])

   
    