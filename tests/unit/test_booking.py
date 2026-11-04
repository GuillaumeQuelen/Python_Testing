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