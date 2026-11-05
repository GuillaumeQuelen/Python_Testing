def test_index_page_is_displayed(client):
    response = client.get('/')
    assert response.status_code == 200


def test_valid_email_shows_summary(client):
    response = client.post('/showSummary', data={'email': 'poor@test.com'})
    assert b"Welcome, poor@test.com" in response.data


def test_logout_redirects_to_index(client):
    response = client.get('/logout')
    assert response.status_code == 302
