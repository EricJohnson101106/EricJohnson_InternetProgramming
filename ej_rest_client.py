# Eric Johnson
# CS47220 - Internet Programming - Summer 2019
# Assignment 5 - Simple REST Client
# Get current weather data for a zip code and print data to a table.
# API Key ERASED
# http://api.openweathermap.org
# installed the requests library https://2.python-requests.org/en/master/
# https://www.w3schools.com/python/python_datetime.asp
# https://stackoverflow.com/questions/12458595/convert-timestamp-since-epoch-to-datetime-datetime

__author__ = "Eric Johnson"

import requests
import datetime


# Function to convert temperature
# ° F = 9/5(K - 273) + 32
def Kelvin_to_Fahrenheit(K):
    return (9.0 / 5.0) * (K - 273) + 32


# Don't know why this is needed but it was requested in the assignment directions
user_id = input("Enter your user ID: ")
user_apiid = input("Enter your API ID: ")
base_url = "http://api.openweathermap.org/data/2.5/weather"
zip_code = input("Enter the ZIP code: ")
complete_url = base_url + "?zip=" + zip_code + "&appid=" + user_apiid

r = requests.get(complete_url)
weather = r.json()

print("Name: \t\t\t\t\t\t" + weather['name'])

current_temp = '{0:.2f}'.format(Kelvin_to_Fahrenheit(weather['main']['temp']))
print("Current Temp (F): \t\t\t" + str(current_temp) + " degrees Fahrenheit")
print("Atmospheric Pressure: \t\t" + str(weather['main']['pressure']) + " hPa")
print("Wind Speed: \t\t\t\t" + str(weather['wind']['speed']) + " meters per second")
print("Wind Direction: \t\t\t" + str(weather['wind']['deg']) + " degrees")
print("Time of Report: \t\t\t" + str(datetime.datetime.fromtimestamp(weather['dt'])))
