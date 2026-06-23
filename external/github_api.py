#OutComing API requests to github ( AI , weather , etc)

import requests

username = "Mohammad"
url = f"http://api.github.com/users/{username}"

response = requests.get(url)   #go get url data


data = response.json()  #convert response to json data
user_info = {
    "username": data["login"],
    "followers": data["followers"],
    "public_repos": data["public_repos"]
}

print(user_info)