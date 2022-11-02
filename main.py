import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("API_KEY_OF_OPEN_WEATHER_MAP")
account_sid = "ACc339a84cef9749acc4c44f8e0522ff1b"
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

weather_params = {
    "lon": 82.4676,
    "lat": 28.3351,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(
    OWM_Endpoint, params=weather_params)

response.raise_for_status()

weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="Hey Manish, Please take an Umbrella. It's been going to rain today!",
        from_='+19705728377',
        to=os.getenv("MY_NUMBER")
    )
    print(message.status)
