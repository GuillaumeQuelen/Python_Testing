def test_cannot_book_more_places_than_points(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Cup',
        'club': 'Poor Club',
        'places': '10',
    })
    assert b"You do not have enough points." in response.data