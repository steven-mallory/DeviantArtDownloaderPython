import secrets
import urllib.parse #urllib.parse.urlencode
from flask import Flask, request #this allows us to receive the GET request to our local server
CLIENT_id = input("Client id\n")


oauthString = "https://www.deviantart.com/oauth2/authorize?" 
state = secrets.token_hex(16)
params = {
    "client_id": CLIENT_id,
    "redirect_uri": "http://localhost:8000/callback",
    "state": state,
    "response_type": "code" 
}
#fullUrl = "&".join([oauthString, "client_id=" + CLIENT_id, "state=" + state, "redirect_uri="redirect_URI])
#fullUrl = oauthString + urllib.parse.urlencode(params)
fullUrl = oauthString + urllib.parse.urlencode(params)


app = Flask(__name__)
@app.route('/')
def index():
    print('args:', request.args)
    return request.args.get('data', 'none')
app.run(port=80, debug=True)
#print(fullUrl)
#get authorization code



