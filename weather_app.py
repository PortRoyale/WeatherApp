# 7/1/2020   Tyler Casper
# I am attempting to build a weather app for my desktop. I am also attempting to use Git version control during this process.

import requests
import json
from tkinter import *


# API 
url = "https://community-open-weather-map.p.rapidapi.com/weather"


# my RapidAPI credentials for Open-Weather's API
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "f51bCvoKijmshiTNqux0PbeIpalLp1NynqDjsngk4K3TgypbZ3"
    }


def fetch_weather(city_state):
    querystring = {"units":"imperial","q":{city_state}}
    response = requests.request("GET", url, headers=headers, params=querystring)
    weather_data = json.loads(response.text)
    return weather_data

def directions(degree_str):
    deg = int(degree_str)
    if (348.75 < deg or degree_str <= 11.25):
        return "N"
    elif (11.25 < deg <= 33.75):
        return "NNE"
    elif (33.75 < deg <= 56.25):
        return "NE"
    elif (56.25 < deg <= 78.75):
        return "ENE"
    elif (78.75 < deg <= 101.25):
        return "E"
    elif (101.25 < deg <= 123.75):
        return "ESE"
    elif (123.75 < deg <= 146.25):
        return "SE"
    elif (146.25 < deg <= 168.75):
        return "SSE"
    elif (168.75 < deg <= 191.25):
        return "S"
    elif (191.25 < deg <= 213.75):
        return "SSW"
    elif (213.75 < deg <= 236.25):
        return "SW"
    elif (236.25 < deg <= 259.75):
        return("WSW")
    elif (258.75 < deg <= 281.25):
        return "W"
    elif (281.25 < deg <= 303.75):
        return "WNW"
    elif (303.75 < deg <= 326.25):
        return "NW"
    elif (326.25 < deg <= 348.75):
        return "NNW"
    else:
        return "N/A"


# TKinter Weather App
window = Tk()
window.title("Weather Application")
# window.geometry('500x200')

lbl = Label(window, text="Enter City, State:")
lbl.grid(column=0, row=0)

txt = Entry(window,width=40)
txt.grid(column=1, row=0)

# Retrieve the city, state data upon click
def clicked():
    city_state = txt.get()
    weather = fetch_weather(city_state)
    print(weather)

    wthr1 = Label(window, text = "Currently: " + weather['weather'][0]['main'] + ", " + weather['weather'][0]['description']) 
    wthr1.grid(column=1, row=3)

    wthr2 = Label(window, text = "Temperature: " + str(weather['main']['temp']) + " F") 
    wthr2.grid(column=1, row=4)

    wthr3 = Label(window, text = "Humidity: " + str(weather['main']['humidity']) + " %") 
    wthr3.grid(column=1, row=5)
    
    wthr4 = Label(window, text = "Wind: " + str(weather['wind']['speed']) + " mph " + directions(weather['wind']['deg'])) 
    wthr4.grid(column=1, row=6)

    wthr5 = Label(window, text = "Clouds: " + str(weather['clouds']['all']) + " % cloudy") 
    wthr5.grid(column=1, row=7)

    # if (weather['weather']['main'] == 'Rain'):
    #     wthr6 = Label(window, text = "Preciptation: " + str(weather['weather']['main']) + " via" + str(weather['weather']['description'])) 
    #     wthr6.grid(column=1, row=7)



btn = Button(window, text="Retrieve Weather", command = clicked)
btn.grid(column=2, row=0)

window.mainloop()


# GOAL: COMPLETED