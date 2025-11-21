import secrets #get state for anti CSRF

redirect = "http://localhost:8000/callback" #can change
client_id = input("What is your client ID?\n")
client_secret = input("What is your client secret? (this will be used because we will use YOUR credentials as a oauth provider)\n")

fullPath = "https://www.deviantart.com/oauth2/authorize?"
random_state = secrets.token_hex(16)
params = {
    "client_id" = client_id,
    "state" = random_state,
    "redirect_uri" = redirect,
    "response_type" = "code"

}
