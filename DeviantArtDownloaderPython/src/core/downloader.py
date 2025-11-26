import urllib.parse
import requests
import sys
import json

from pathlib import Path #writing 


#let's say we have a token now, read it somehow

with open("token.json", "r") as f:
    ACCESS_TOKEN = json.load(f)["access_token"]

params = {
        "access_token": ACCESS_TOKEN
}

if input("Do you want to specify a user's favourites? (y/N)\n").lower() == 'y':
    params["username"] = input("Please specify the username\n")


#print(json.dumps(response, indent=4))

devURL = "https://www.deviantart.com/api/v1/oauth2/collections/all?" + urllib.parse.urlencode(params)
params["limit"] = 24 #24 per page, as per API. use offset after to nto download the same thing over and over
directory = Path("DeviantArtDownloads")
directory.mkdir(parents=True, exist_ok=True)

count = 0;
while True:
    response = requests.get(devURL, params=params).json()

    for item in response["results"]: #I think this already finds all the favourites
        print(json.dumps(item, indent=4))
        
        # download
        
        #devID = item["deviationid"]
        
        #dlUrl = f"https://www.deviantart.com/api/v1/oauth2/deviation/download/{devID}"

        #response2 = requests.get(dlUrl, params=params).json()
        response2 = item["content"]
        #print(response2.keys())
        if "src" not in response2:
            print("Did not find 'src' in", response2)
            continue
        url = response2["src"]
        img_data = requests.get(url).content
        t = url.split("/")[-1].split("?")[0]
        ext = Path(t).suffix
        print(f"LOOOL {ext}")
        with open(directory / f"{count}{ext}", "wb") as f:
            f.write(img_data)
        count = count + 1 
    if not response.get("has_more"):
        break
    params["offset"] = response["next_offset"]
    


    



def logout():
    requests.post("https://www.deviantart.com/oauth2/revoke?access_token=" + ACCESS_TOKEN)
