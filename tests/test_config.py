from config import CLUBS_FILE, COMPETITIONS_FILE

def test_config_constants():
    assert CLUBS_FILE == 'data/clubs.json'
    assert COMPETITIONS_FILE == 'data/competitions.json'
