import requests
import json
from pathlib import Path
#from config import config
#from src import config
from DeviantArtDownloaderPython.src import config



def load_session_from_cookies():
    session = requests.Session()

    with open(COOKIES_FILE, 'r') as f:
        json.load(f, cookies)
