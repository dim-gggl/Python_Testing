import json

__all__ = ['load_clubs', 'load_competitions']

SECRET_KEY = 'something_special'

def load_clubs():
    with open('data/clubs.json', 'r') as c:
         list_of_clubs = json.load(c)['clubs']
         return list_of_clubs

def load_competitions():
    with open('data/competitions.json', 'r') as comps:
         list_of_competitions = json.load(comps)['competitions']
         return list_of_competitions