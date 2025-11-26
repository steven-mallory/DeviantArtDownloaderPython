import secrets
import urllib.parse #urllib.parse.urlencode
from flask import Flask, request #this allows us to receive the GET request to our local server
from flask import redirect #used for step 1, need to tell user to go and login!
import requests #used for step 4, 5
from DeviantArtDownloaderPython.src.config import CONFIG

import json
from flask import jsonify #so that test 45 works

# STEPS
#1: Redirect user to Login
#2: DeviantArt sends an auth code to redirect_uri.
#3: Listen in to redirect_uri callback, extract auth code
#4: Send POST to token endpoint, include client_secret this time
#5: Receive access code through JSON returned by DeviantArt


# STEP 1
#1: Redirect user to Login

oauthString = "https://www.deviantart.com/oauth2/authorize?" 
state = secrets.token_hex(16)

print("----------------------INSTRUCTIONS\n-----------------------Please visit", "localhost:8000/login", "in your browser\n------------------------------------------------------") 

app = Flask(__name__)
@app.route('/login')
def login():
    #POST TO fullUrl
    params = {
        "client_id": CONFIG["client_id"],
        "redirect_uri": "http://localhost:8000/callback",
        "state": state,
        "response_type": "code" ,
        "scope": "browse collection"
    }
    fullUrl = oauthString + urllib.parse.urlencode(params)
    print(fullUrl)
    return redirect(fullUrl) #login, flasa

# STEP 2 is implicit, done by DA
#2: DeviantArt sends an auth code to redirect_uri.


# STEP 3
#3: Listen in to redirect_uri callback, extract auth code


@app.route(urllib.parse.urlparse(CONFIG["redirect_uri"]).path)
def callback():
    AUTH_CODE = request.args.get('code')
    if (AUTH_CODE == None):
        raise Exception("Code not found")


    # STEP 4
    #4: Send POST to token endpoint, include client_secret this time
    

    tokenEndpoint = "https://www.deviantart.com/oauth2/token"
    params = {
        "client_id": CONFIG["client_id"],
        "redirect_uri": CONFIG["redirect_uri"],
        "grant_type": "authorization_code",
        "code": AUTH_CODE,
        #dont share
        "client_secret": CONFIG["client_secret"]
    }
    x = requests.post(tokenEndpoint, params)  #this will be tested using mocker.patch, whatever that means
    # STEP 5 
    #5: Receive access code through JSON returned by DeviantArt
    try:
        accessToken = x.json().get("access_token") #WOOO!!
        data = {"access_token": accessToken}
        try:
            with open("token.json", "w") as f:
                json.dump({"access_token": accessToken}, f)
        except Exception as e:
            data["FILE IO"] = "FAILED, PLEASE COPY" 
            data["ERROR"] = f"{e}"
        return jsonify(data) #jsonify, basically a response object
        
    except:
        return jsonify({"error": "no access token found"}), 500

if __name__ == "__main__":
    app.run(port=8000, debug=True)

        #reading from the GET request
#print(fullUrl)
#get authorization code

