from app import app

def test_info():
    tester = app.test_client()
    response = tester.get('/info')
    assert response.status_code == 200
    assert b"hi i am info function" in response.data

def test_phone():
    tester = app.test_client()
    response = tester.get('/phone')
    assert response.status_code == 200
    assert b"1234567890" in response.data
