import secrets
import urllib.parse #urllib.parse.urlencode
from flask import Flask, request #this allows us to receive the GET request to our local server
from flask import redirect #used for step 1, need to tell user to go and login!
import requests
from DeviantArtDownloaderPython.src.config import CONFIG

CLIENT_id = input("Client id\n")

# STEPS
#1: Redirect user to Login
#2: DeviantArt sends an auth code to redirect_uri.
#3: Listen in to redirect_uri callback, extract auth code
#4: Send POST to token endpoint, include client_secret this time
#5: Receive access code through JSON returned by DeviantArt


# STEP 1

oauthString = "https://www.deviantart.com/oauth2/authorize?" 
state = secrets.token_hex(16)

app = Flask(__name__)
@app.route('/login')
def login():
    #POST TO fullUrl
    params = {
        "client_id": CLIENT_id,
        "redirect_uri": "http://localhost:8000/callback",
        "state": state,
        "response_type": "code" 
    }
    fullUrl = oauthString + urllib.parse.urlencode(params)
    print("Please visit", CONFIG["redirect_uri"], "in your browser") 
    return redirect(fullUrl) #login

# STEP 2 is implicit, done by DA


# STEP 3


@app.route(urlparse(CONFIG["redirect_uri"]).path)
def callback():
    AUTH_CODE = request.args.get('code')
    if (AUTH_CODE == None):
        raise Exception("Code not found")


    # STEP 4
    

    tokenEndpoint = "https://www.deviantart.com/oauth2/token"
    params = {
        "client_id" = CONFIG["client_id"],
        "redirect_uri" = CONFIG["redirect_uri"],
        "grand_type" = "authorization_code",
        "code" = AUTH_CODE,
        #dont share
        "client_secret" = CONFIG["client_secret"]
    }
    x = requests.post(url, json = jsonOBJ)
    jsonOBJ = x.json()
    
    # STEP 5 
    try:
        accessToken = x.json().get("access_token") #WOOO!!
    except:
        print("Did not find access_token")

app.run(port=80, debug=True)

        #reading from the GET request
#print(fullUrl)
#get authorization code

