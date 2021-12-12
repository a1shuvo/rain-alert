import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "047b69d878db08a330e6e00568009769"
LAT = 24.743448
LONG = 90.398384

t = "https://api.openweathermap.org/data/2.5/onecall?" \
    "lat=24.743448&lon=90.398384&exclude=currently,minutely,daily,alerts&appid=047b69d878db08a330e6e00568009769"

parameters = {
    "lat": 59.937500,
    "lon": 30.308611,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring An Umbrella!")


