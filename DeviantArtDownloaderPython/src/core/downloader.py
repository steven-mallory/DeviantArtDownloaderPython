import urllib.parse
import requests

import json

from path import Path #writing 

#let's say we have a token now, read it somehow

with open("token.json", "r") as f:
    ACCESS_TOKEN = json.load(f)["access_token"]

params = {
        "access_token": ACCESS_TOKEN
}

if input("Do you want to specify a user's favourites? (y/N)\n").lower() == 'y':
    params["username"] = input("Please specify the username\n")

#collectionsFolderURL = "https://www.deviantart.com/api/v1/oauth2/collections/folders?" + urllib.parse.urlencode(params)
collectionsFolderURL = "https://www.deviantart.com/api/v1/oauth2/collections/all?" + urllib.parse.urlencode(params)
response = requests.get(collectionsFolderURL)
print(response.status_code)
print(json.dumps(response.json(), indent=4))
for folder in response["results"]:
    if folder["name"] == "favourites":
        print(folder)
        favFolderID = folder["folderid"]
        break

#need test casefor folder
devURL = f"https://www.deviantart.com/api/v1/oauth2/collections/{favFolderID}"
params["limit"] = 24 #24 per page, as per API. use offset after to nto download the same thing over and over

directory = Path("DeviantArtDownloads")
directory.mkdir(exist_ok=True)
while True:
    response = requests.get(devURL, params=params).json()
    if not response.get("has_more"):
        break

    
    # download
    for item in response["results"]:
        devID = item["deviationid"]
        dlUrl = f"https://www.deviantart.com/api/v1/oauth2/deviation/download/{devID}"

        response2 = requests.get(dlUrl, params=params).json()
        if "src" not in response2:
            print("Did not find 'src' in", response2)
            continue
        url = response2["src"]
        img_data = requests.get(url).content

        with open(directory / url.split("/")[-1], "wb") as f:
            f.write(img_data)
    


    params["offset"] = response["next_offset"]

#/gallery/{folderid}
#for _ in range

    

def download(devID):
    x = 5     




def logout():
    requests.post("https://www.deviantart.com/oauth2/revoke?access_token=" + ACCESS_TOKEN)
