import datetime
import json

import requests
from flask import Flask

app = Flask(__name__)


@app.route('/sun/')
def sun_info():
    header = {"x-access-token": "9a1770975b443e98b4f04a27eead7eb8"}
    day = datetime.date.today()
    url = 'https://api.openuv.io/api/v1/uv?lat=56.33&lng=44.01&dt=' + str(day)
    response = requests.get(url, headers=header)
    info = json.loads(response.text)['result']['sun_info']['sun_times']
    sunrise = info['sunrise']
    sunset = info['sunset']
    sunrise = datetime.datetime.strptime(sunrise.split('T')[1][:-5], '%H:%M:%S') + datetime.timedelta(hours=3)
    sunset = datetime.datetime.strptime(sunset.split('T')[1][:-5], '%H:%M:%S') + datetime.timedelta(hours=3)

    return f"Today sunrise: {sunrise.time()} sunset: {sunset.time()}"


@app.route('/oil/')
def oil_info():
    response = requests.get('https://www.quandl.com/api/v3/datasets/OPEC/ORB.csv?api_key=yrdNaxD7ooqADcvpQBw8')
    oil_price = response.text.split('\n')[1].split(',')[1]
    return f"Price of oil for today is {oil_price}"
