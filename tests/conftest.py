import pytest
import server
from server import app


@pytest.fixture(autouse=True)
def fake_data(monkeypatch):
    clubs = [
        {"name": "Poor Club", "email": "poor@test.com", "points": "4"},
        {"name": "Rich Club", "email": "rich@test.com", "points": "30"},
    
    ]
    competitions = [
            {"name": "Future Cup", "date": "2099-01-01 10:00:00", "numberOfPlaces": "25"},
            {"name": "Small Cup", "date": "2099-01-01 10:00:00", "numberOfPlaces": "3"},
        ]
    monkeypatch.setattr(server, "clubs", clubs)
    monkeypatch.setattr(server, "competitions", competitions)
    monkeypatch.setattr(server, "bookings", {}, raising=False)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client