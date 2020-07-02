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

    wthr2 = Label(window, text = weather['main']) 
    wthr2.grid(column=1, row=3)
    
    wthr3 = Label(window, text = weather['wind']) 
    wthr3.grid(column=1, row=4)

btn = Button(window, text="Retrieve Weather", command = clicked)
btn.grid(column=2, row=0)

window.mainloop()


# GOAL: COMPLETED