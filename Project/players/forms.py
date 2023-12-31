from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, DecimalField, TextAreaField, validators, SubmitField
from wtforms.validators import URL

class PlayerFetchForm(FlaskForm):
   
    plrN = StringField('Player Name', [validators.Length(min=1, max=20)])
    
    

class PlayerSearchForm(FlaskForm):
    class Meta:
        # This overrides the value from the base form.
        csrf = False
    #symbol = StringField('Symbol', [validators.Length(min=1, max=10)])
    #plrN = StringField('Player Name', [validators.Length(min=1, max=255)])
    player_id = StringField('Player_id')
    
    name = StringField('name')
    team_name = StringField('team_name')
    face_image_id = StringField('face_image_id')
    limit = IntegerField("Limit", default=10)
    sort = SelectField("Sort")
    order = SelectField("Order", choices=[("asc","+"), ("desc","-")])
    submit = SubmitField("Filter")

class PlayerForm(FlaskForm):
    player_id = StringField('Player ID', [
        validators.Length(min=1, max=255, message='Player ID must be between 1 and 255 characters'),
        validators.Regexp('^[0-9]+$', message='Player ID can only contain numbers')
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
        validators.Regexp('^[0-9]+$', message='Face Image ID can only contain numbers ')
    ])
    source = StringField('Source', [validators.Length(min=1, max=255)])
    submit = SubmitField("Save")

class AdminPlayerSearchForm(PlayerSearchForm):
    username = StringField("Username")

class AssocForm(FlaskForm):
    class Meta:
        # This overrides the value from the base form.
        csrf = False
    username = StringField("Username")
    player = StringField("Player Name")
    submit = SubmitField("Filter")