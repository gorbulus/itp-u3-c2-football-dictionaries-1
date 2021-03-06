# assignment_3.py
# William Ponton 1.161.21
# Football Dictionaries Project

# IMport packages
from .assignment_1 import players_as_dictionaries

# players_by_country _and_position
# groups players by position and country
def players_by_country_and_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    player_country = {}

    for player in squad:
        country = player["country"]
        position = player["position"]
        player_country.setdefault(country, {})
        player_country[country].setdefault(position, [])
        player_country[country][position].append(player)
    return player_country