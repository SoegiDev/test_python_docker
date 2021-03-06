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
    
@pytest.mark.parametrize('say',['fajar soegi'])
@pytest.mark.parametrize('age',[14])
def test_say_age(web, say,age):
    response = web.get(f'/say/age/{say}/{age}')
    assert response.status_code == 200
    assert response.data == b'Hello, Hallo fajar soegi 14'
    
def test_mywife(web):
    response = web.get('/mywife')
    assert response.status_code == 200
    assert response.data == b'Hello, Eva'