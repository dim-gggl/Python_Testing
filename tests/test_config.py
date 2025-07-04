from config import load_clubs, load_competitions


def test_load_clubs_returns_list():
    clubs = load_clubs()
    assert isinstance(clubs, list)

def test_load_competitions_returns_list():
    competitions = load_competitions()
    assert isinstance(competitions, list)

def test_load_clubs_returns_correct_number_of_clubs():
    clubs = load_clubs()
    assert len(clubs) == 3

def test_load_competitions_returns_correct_number_of_competitions():
    competitions = load_competitions()
    assert len(competitions) == 2

def test_load_clubs_returns_correct_club_data():
    clubs = load_clubs()
    assert clubs[0]['name'] == 'Simply Lift'
    assert clubs[0]['email'] == 'john@simplylift.co'
    assert clubs[0]['points'] == '13'
    assert clubs[1]['name'] == 'Iron Temple'
    assert clubs[1]['email'] == 'admin@irontemple.com'
    assert clubs[1]['points'] == '4'
    assert clubs[2]['name'] == 'She Lifts'
    assert clubs[2]['email'] == 'kate@shelifts.co.uk'
    assert clubs[2]['points'] == '12'

def test_load_competitions_returns_correct_competition_data():
    competitions = load_competitions()
    assert competitions[0]['name'] == 'Spring Festival'
    assert competitions[0]['date'] == '2020-03-27 10:00:00'
    assert competitions[0]['number_of_places'] == '25'
    assert competitions[1]['name'] == 'Fall Classic'
    assert competitions[1]['date'] == '2020-10-22 13:30:00'
    assert competitions[1]['number_of_places'] == '13'