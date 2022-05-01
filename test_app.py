# test_hello.py
import app
import pytest

@pytest.fixture()
def web():
    return app.app.test_client()

def test_hello(web):
    response = web.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, Docker!'
    

@pytest.mark.parametrize('number',[12])
def test_number(web, number):
    response = web.get(f'/number/{number}')
    assert response.status_code == 200
    assert response.data == b'Hello,Your NUmber is 12'
    

@pytest.mark.parametrize('say',['Fajar Soegi'])
def test_say(web, say):
    response = web.get(f'/say/{say}')
    assert response.status_code == 200
    assert response.data == b'Hello, Hai Fajar Soegi'
    
