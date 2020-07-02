# 7/1/2020   Tyler Casper
# I am attempting to build a weather app for my desktop. I am also attempting to use Git version control during this process.

import requests
import json
from tkinter import *


# API 
url = "https://community-open-weather-map.p.rapidapi.com/weather"


# my RapidAPI credentials
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "f51bCvoKijmshiTNqux0PbeIpalLp1NynqDjsngk4K3TgypbZ3"
    }


# TKinter
window = Tk()

window.title("Weather Application")
window.geometry('400x250')

lbl = Label(window, text="Enter City, State:")
lbl.grid(column=0, row=4)

# Retrieve the city, state data upon click
def clicked():
    city = txt.get()
    querystring = {"units":"imperial","q":{city}}
    response = requests.request("GET", url, headers=headers, params=querystring)
    dictionary = json.loads(response.text)
    print(dictionary)

btn = Button(window, text="Retrieve Weather", command = clicked)
btn.grid(column=2, row=4)

txt = Entry(window,width=30)
txt.grid(column=1, row=4)
txt.focus()

window.mainloop()



