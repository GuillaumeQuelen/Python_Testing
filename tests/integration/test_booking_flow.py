def test_login_book_and_see_points_on_board(client):
    # 1. Le club se connecte
    response = client.post('/showSummary', data={'email': 'rich@test.com'})
    assert b"Welcome, rich@test.com" in response.data

    # 2. Il ouvre la page de réservation
    response = client.get('/book/Future%20Cup/Rich%20Club')
    assert b"Future Cup" in response.data

    # 3. Il réserve 5 places
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Cup',
        'club': 'Rich Club',
        'places': '5',
    })
    assert b"Great-booking complete!" in response.data
    assert b"Points available: 25" in response.data

    # 4. Le tableau public affiche ses nouveaux points
    response = client.get('/points')
    assert b"<td>25</td>" in response.data