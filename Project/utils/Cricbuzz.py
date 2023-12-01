import os
# fix for testing just this file
if __name__ == "__main__":
   
    import sys
    # Get the parent directory of the current script (api.py)
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    PARENT_DIR = os.path.join(CURR_DIR, "..")  # Go up one level from utils to project folder
    sys.path.append(PARENT_DIR)
from utils.api import API
class Cricbuzz(API):
    @staticmethod
    def get_player_stats(player_name):
        params = {"plrN":player_name}
        #params["function"] = "GLOBAL_QUOTE"
        
        #params["datatype"] = "json"
        url = "/stats/v1/player/search"
        resp = API.get(url, params)
        players =[]
        # this API is "odd" and includes numbers as part of the keys like 01. 02. 03. etc and below removes that and returns just the named keys
        # below also converts the remaining spaces into _ to avoid space problems
        # I think the API is mostly targeted at the csv output option instead of the json option although it supports both
        if "player" in resp and isinstance(resp["player"], list):
            players = resp["player"]

        return players

        

if __name__ == "__main__":
    player_name = "Sachin"
    players = Cricbuzz.get_player_stats(player_name)
    

    if players:
        for player in players:
            print(f"Player ID: {player['id']}, Name: {player['name']}, Team: {player['teamName']}")
    else:
        print("No players found.")