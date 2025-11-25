from pathlib import Path
print(Path)
from DeviantArtDownloaderPython.src.core.gettingToken import app


def test_step1():
    client = app.test_client() #flask allows us to use test client to
    response = client.get("/login")
    
    assert response.status_code == 302

    assert "deviantart.com/oauth2/authorize" in response.headers["Location"]

def test_step3(): #2 implicit
    client = app.test_client()
    response = client.get("/callback")

    assert response.status_code == 500

def test_step45(mocker): #mocker is like bypassing decorator syntax, something pytest-mock installed
    client = app.test_client()

    class MockAPIPost:
        def json(self):
            return {"access_token": "blahblahLOOL!"}

    mocker.patch("requests.post", return_value=MockAPIPost()) 

    resp = client.get("/callback?code=fakeDumbStuff")
    assert resp != None
    assert resp.status_code == 200
    assert resp.json["access_token"] == "blahblahLOOL!"
    
