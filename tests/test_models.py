import pytest
from models import Club, Competition, CompetitionPlace


class TestClub:
    """Tests for the Club class"""
    
    def test_club_initialization(self):
        club = Club("Test Club", "test@club.com", "10")
        assert club.name == "Test Club"
        assert club.email == "test@club.com"
        assert club.points == 10
        assert club.competition_places == []
    
    def test_add_competition_place_valid(self):
        club = Club("Test Club", "test@club.com", "10")
        competition = Competition("Test Compet", "2025-07-03 10:00:00", "20")
        place = CompetitionPlace(competition)
        
        club.add_competition_place(place, 5)
        
        assert len(club.competition_places) == 1
        assert club.competition_places[0].number == 5
        assert club.competition_places[0].competition.name == "Test Compet"
    
    def test_get_competition_places(self):
        club = Club("Test Club", "test@club.com", "10")
        competition = Competition("Test Compet", "2025-07-01 10:00:00", "20")
        place = CompetitionPlace(competition)
        
        club.competition_places = [place.add_number(5)]
        
        places = club.get_competition_places()
        assert places == club.competition_places
        assert len(places) == 1


class TestCompetition:
    """Tests for the Competition class"""
    
    def test_competition_initialization(self):
        competition = Competition("Test Compet", "2025-06-30 10:30:00", "20")
        assert competition.name == "Test Compet"
        assert competition.date == "2025-06-30 10:30:00"
        assert competition.number_of_places == 20
    
    def test_is_complete_false(self):
        competition = Competition("Test Compet", "2025-09-22 10:00:00", "20")
        assert not competition.is_complete
    
    def test_is_complete_true(self):
        competition = Competition("Test Compet", "2025-10-10 10:00:00", "0")
        assert competition.is_complete
