import secrets
import urllib.parse
import Flask #this allows us to receive the GET request to our local server
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



print(fullUrl)
#get authorization code



