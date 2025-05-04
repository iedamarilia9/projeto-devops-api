# test_app.py

from app import app

def test_home_status_code():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_content_type():
    tester = app.test_client()
    response = tester.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

def test_home_data():
    tester = app.test_client()
    response = tester.get('/')
    assert b"Bem-vindo" in response.data

def test_404():
    tester = app.test_client()
    response = tester.get('/naoexiste')
    assert response.status_code == 404

def test_post_sem_dados():
    tester = app.test_client()
    response = tester.post('/alguma-rota', data={})
    assert response.status_code in [400, 200]  # Depende da sua lógica
