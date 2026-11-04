def test_points_board_shows_all_clubs_and_points(client):
    response = client.get('/points')
    assert response.status_code == 200
    assert b"Poor Club" in response.data
    assert b"Rich Club" in response.data
    assert b"30" in response.data