import json
from models import Club, Competition
from config import CLUBS_FILE, COMPETITIONS_FILE


def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_to_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, ensure_ascii=True, indent=4)


class DataManager:
    """
    Centralized data manager
    Loads data from files and provides access to it
    """
    
    def __init__(self):
        self._clubs = None
        self._competitions = None

    def load_clubs(self):
        list_of_clubs = load_data(CLUBS_FILE)['clubs']
        list_of_clubs = [
            Club(
                elem["name"],
                elem["email"],
                elem["points"]
            ) for elem in list_of_clubs
        ]
        return list_of_clubs
    
    def load_competitions(self):
        list_of_competitions = load_data(COMPETITIONS_FILE)['competitions']
        list_of_competitions = [
            Competition(
                elem["name"],
                elem["date"],
                elem["number_of_places"]
            ) for elem in list_of_competitions
        ]
        return list_of_competitions

    @property
    def clubs(self):
        if self._clubs is None:
            self._clubs = self.load_clubs()
        return self._clubs
    
    @property
    def competitions(self):
        if self._competitions is None:
            self._competitions = self.load_competitions()
        return self._competitions

    def find_club_by_email(self, email):
        for club in self.clubs:
            if club.email == email:
                return club
        return None
    
    def find_club_by_name(self, name):
        for club in self.clubs:
            if club.name == name:
                return club
        return None
    
    def find_competition_by_name(self, name):
        for competition in self.competitions:
            if competition.name == name:
                return competition
        return None
    
    def reload_data(self):
        """Reload data from files"""
        self._clubs = self.load_clubs()
        self._competitions = self.load_competitions()
    
    def save_data(self):
        """Save data to files"""
        clubs_dict = [club.to_dict() for club in self.clubs]
        competitions_dict = [competition.to_dict() for competition in self.competitions]

        data = {"clubs": clubs_dict}
        data2 = {"competitions": competitions_dict}

        save_to_json(data, CLUBS_FILE)
        save_to_json(data2, COMPETITIONS_FILE)
