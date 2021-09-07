import os
import requests
from requests_oauthlib import OAuth1
import dotenv

dotenv.load_dotenv()

auth = OAuth1(os.getenv("KEY"),
              os.getenv("SECRET"))
endpoint = "http://api.thenounproject.com/icon/sun"

response = requests.get(endpoint, auth=auth)
res = response.json()
print(res)
url_icon = res["icon"]["icon_url"]

response_icon = requests.get(url_icon)
icon_bytes = response_icon.content
with open("icons/test.svg", "wb") as file:
    file.write(icon_bytes)
