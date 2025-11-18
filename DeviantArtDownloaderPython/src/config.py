import json
from pathlib import Path
#with open("../config/config.json", 'r') as f
CONFIG_JSON_PATH = Path(__file__).parent.parent / "config" / "config.json"
with open(CONFIG_JSON_PATH, 'r') as f:
    CONFIG = json.load(f)

COOKIES_FILE = CONFIG["cookie_file"] #this is my var
