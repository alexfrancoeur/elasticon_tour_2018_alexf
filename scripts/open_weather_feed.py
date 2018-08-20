#!/usr/bin/python
from pyowm import OWM
import elasticsearch
import pprint
import time

owm = OWM("9bea2c347bc2633ce808e3581ce238e5")
es = elasticsearch.Elasticsearch(['localhost'],port=9400,http_auth=("elastic","Elastic2018!"))

mapping = {
    "mappings" : {
            "weather_obs" : {
                "properties" : {
                        "timestamp" : { "type" : "date" },
                        "clouds" : { "type" : "long" },
                        "rain"   : {
                            "properties" : {
                                "3h": {"type": "long"}
                                }
                        },
                        "snow"   : {
                            "properties" : {
                                "3h": {"type": "long"}
                                }
                        },
                        "wind" : {
                            "properties" : {
                                "speed" : {"type":"float"},
                                "gust" : {"type":"float"},
                                "deg" : {"type":"long"}
                                }
                        },
                        "humidity" : {"type":"long"},
                        "pressure" : {
                            "properties" : {
                                "press" : {"type":"long"},
                                "sea_level" : {"type": "text"}
                                }
                        },
                        "temperature" : {
                            "properties" : {
                                "temp": {"type":"float"},
                                "temp_kf": {"type":"float"},
                                "temp_max": {"type":"float"},
                                "temp_min": {"type":"float"}
                            }
                        },
                        "short_description" : {"type":"keyword"},
                        "long_description" : {"type":"text"},
                        "place" : {"type":"keyword"},
                        "location" : {"type":"geo_point"}
                }
            }
    }
}

pprint.pprint(mapping)

es.indices.create(index="weather",body=mapping, ignore=400)

while True:
    for place in ['London, GB']:
        try:
            weather_doc = {}
            obs = owm.weather_at_place(place)

            weather = obs.get_weather()

            weather_doc['timestamp'] = weather.get_reference_time(timeformat='iso').replace(' ','T')
            weather_doc['clouds'] = weather.get_clouds()
            weather_doc['rain'] = weather.get_rain()
            weather_doc['snow'] = weather.get_snow()
            weather_doc['wind'] = weather.get_wind()
            weather_doc['humidity'] = weather.get_humidity()
            weather_doc['pressure'] = weather.get_pressure()
            weather_doc['temperature'] = weather.get_temperature(unit='fahrenheit')
            weather_doc['short_description'] = weather.get_status()
            weather_doc['long_description'] = weather.get_detailed_status()
            weather_doc['place'] = place

            location = obs.get_location()

            weather_doc['location'] = { "lat": location.get_lat(), "lon": location.get_lon() }
            es.index(index="weather", doc_type="weather_obs", id=weather_doc['place']+weather_doc['timestamp'], body=weather_doc)

            pprint.pprint(weather_doc['place']+weather_doc['timestamp'])
            pprint.pprint(weather_doc)
        except:
            print "Error contacting web service"
        time.sleep(1)
    print "sleeping for 15"
    time.sleep(15*60)
