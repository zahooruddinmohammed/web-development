from datetime import datetime
from decimal import Decimal
from common.utils import JsonSerializable

class CricketPlayer(JsonSerializable):
    def __init__(self, player_id: str, name: str, team_name: str, face_image_id: str,
                 created: datetime = None, modified: datetime = None):
        self.player_id = player_id
        self.name = name
        self.team_name = team_name
        self.face_image_id = face_image_id
        self.created = created
        self.modified = modified
