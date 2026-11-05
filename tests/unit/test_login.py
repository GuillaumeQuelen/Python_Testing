def test_unknown_email_message(client):
    response = client.post('/showSummary', data={'email': 'inconnu@something.com'})
    assert response.status_code == 200
    assert b"Sorry, this email is unknown." in response.data
