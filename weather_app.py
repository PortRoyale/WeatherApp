# 7/1/2020   Tyler Casper
# I am attempting to build a weather app for my desktop. I am also attempting to use Git version control during this process.

import requests, json

url = "https://community-open-weather-map.p.rapidapi.com/weather"

city = "Springfield, Illinois"

querystring = {"units":"imperial","q":{city}}


# my RapidAPI credentials
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "f51bCvoKijmshiTNqux0PbeIpalLp1NynqDjsngk4K3TgypbZ3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

d = json.loads(response.text)
print(d)