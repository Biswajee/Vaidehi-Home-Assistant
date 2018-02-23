from flask import Flask, request
from flask import jsonify

import requests
# Instantiating Flask object
app = Flask(__name__)


@app.route('/')
def index():
    send = {
        "messages": [
            {"text": "Hi there {{ first name }} "}
        ]
    }
    return jsonify(send)


@app.route('/weather')
def weather():
    lat = request.args['latitude']
    lon = request.args['longitude']
    result = get_details(lat, lon)
    desc, humidity, clouds, wind_speed, icon = result
    print(lat)
    print(lon)
    if result != 'fail':
        send = {
        "messages": [
            {
                "text": "description: " + desc
            },
            {
                 "text": "Humidity: " + str(humidity)   
            },
            {
                 "text": "Clouds:" + str(clouds) 
            },
            {
                 "text" : "Wind Speed:" + str(wind_speed)
            },
            {
      "attachment": {
        "type": "image",
        "payload": {
          "url": "http://openweathermap.org/img/w/" + icon + ".png"
        }
      }
    }
        
        ]
    }
    else:
        {
	        "messages": [
	            {
	      		"text": "Couldn't found anything related to that."
	    	}
	        ]
	    }
            
    return jsonify(send)

def get_details(lat,lon):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID=fd6bd451522e8dd7d5c5a850ec64e591".format(lat, lon))
    if r.status_code != 200:
        return "Fail"
    else:
        data = r.json()
        result = (data['weather'][0]['description'], data['main']['humidity'], data['clouds']['all'], data['wind']['speed'], data['weather'][0]['icon'])
        return result
    
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RV'
if __name__ == "__main__":
    app.run(port=5000)