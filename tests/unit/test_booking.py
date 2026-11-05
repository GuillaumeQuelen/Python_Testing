import pytest

def test_cannot_book_more_places_than_points(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Cup',
        'club': 'Poor Club',
        'places': '10',
    })
    assert b"You do not have enough points." in response.data

def test_points_are_deducted_after_booking(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Cup',
        'club': 'Poor Club',
        'places': '3',
    })
    assert b"Points available: 1" in response.data

def test_cannot_book_more_places_than_available(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Small Cup',
        'club': 'Rich Club',
        'places': '5',
    })
    assert b"Not enough places left in this competition." in response.data

def test_cannot_book_more_than_12_places(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Cup',
        'club': 'Rich Club',
        'places': '13',
    })
    assert b"You cannot book more than 12 places per competition." in response.data

def test_cannot_book_more_than_12_places_in_total(client):
    data = {'competition': 'Future Cup', 'club': 'Rich Club', 'places': '8'}
    client.post('/purchasePlaces', data=data)
    response = client.post('/purchasePlaces', data=data)
    assert b"You cannot book more than 12 places per competition." in response.data

def test_cannot_book_a_past_competition(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Old Cup',
        'club': 'Rich Club',
        'places': '1',
    })
    assert b"This competition is over: booking is closed." in response.data


def test_cannot_open_booking_page_of_past_competition(client):
    response = client.get('/book/Old%20Cup/Rich%20Club')
    assert b"This competition is over: booking is closed." in response.data

def test_book_unknown_competition_shows_message(client):
    response = client.get('/book/Nope/Rich%20Club')
    assert b"Something went wrong-please try again" in response.data


def test_book_unknown_club_shows_message(client):
    response = client.get('/book/Future%20Cup/Nobody')
    assert b"Something went wrong-please try again" in response.data


@pytest.mark.parametrize("places", ["", "abc", "0", "-3"])
def test_invalid_places_are_refused(client, places):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Cup',
        'club': 'Rich Club',
        'places': places,
    })
    assert b"Please enter a valid number of places." in response.data

def test_purchase_unknown_competition_shows_message(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Nope',
        'club': 'Rich Club',
        'places': '1',
    })
    assert b"Something went wrong-please try again" in response.data


def test_purchase_unknown_club_shows_message(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Cup',
        'club': 'Nobody',
        'places': '1',
    })
    assert b"Something went wrong-please try again" in response.data
    