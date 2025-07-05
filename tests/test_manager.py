from manager import DataManager

data_manager = DataManager()

def test_clubs():
    clubs = data_manager.load_clubs()
    assert len(clubs) == 3
    assert clubs[0].name == "Simply Lift"
    assert clubs[0].email == "john@simplylift.co"

    assert clubs[1].name == "Iron Temple"
    assert clubs[1].email == "admin@irontemple.com"

    assert clubs[2].name == "She Lifts"
    assert clubs[2].email == "kate@shelifts.co.uk"


def test_competitions():
    competitions = data_manager.load_competitions()
    assert len(competitions) == 2
    assert competitions[0].name == "Spring Festival"
    assert competitions[0].date == "2020-03-27 10:00:00"

    assert competitions[1].name == "Fall Classic"
    assert competitions[1].date == "2020-10-22 13:30:00"

def test_find_club_by_email():
    club = data_manager.find_club_by_email("john@simplylift.co")
    assert club.name == "Simply Lift"

def test_find_competition_by_name():
    competition = data_manager.find_competition_by_name("Spring Festival")
    assert competition.date == "2020-03-27 10:00:00"

def test_find_club_by_name():
    club = data_manager.find_club_by_name("Simply Lift")
    assert club.email == "john@simplylift.co"