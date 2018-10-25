import requests
import time
import json
import WeatherForecasting
import sys
import datetime
city=input("enter your city name\n")
ddict = {}
app_id=input("Please input valid API key")
app_id=app_id.replace("\"",'')
app_id=app_id.replace(" ",'')


weather_url="http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}".format(city,app_id)
resp=requests.get(weather_url)

text=json.loads(resp.text)

print("------------------------------------Here are the Weather details for All 5 days with every 3 hours of span------------------------------------")

WeatherForecasting.day1(**text)
WeatherForecasting.day2(**text)
WeatherForecasting.day3(**text)
WeatherForecasting.day4(**text)
WeatherForecasting.day5(**text)

print("Data stored to file WeatherForecast.txt")

try:
    print("Press Ctrl + C to quit")
    time.sleep(300)

    # keypress=input("Press Ctrl + C to quit")

except KeyboardInterrupt:

    print("Good Bye")

sys.stdout= open('WeatherForecast.txt','w')

print("                 Data Requested on ", datetime.datetime.now()              )


WeatherForecasting.day1(**text)
WeatherForecasting.day2(**text)
WeatherForecasting.day3(**text)
WeatherForecasting.day4(**text)
WeatherForecasting.day5(**text)

sys.stdout.close()



