import requests
import json
import datetime
import time
from Twitter_Handler import Twitter_Handler

########################### TO DO ######################
# Integrate with code to interact with Twitter API
# Call twitter api if True
# Create Proof of concept example to present in the class (time frame where ony 1 incident ocurred, to ensure that the api is called,
# just set oldTime to whatever I need in order for it to show up)

# important links:
# https://earthquake.usgs.gov/fdsnws/event/1/
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

class USGS_weather_api_call(object):
    oldTime: str
    newTime: str
    requestString: str
    twitter: Twitter_Handler

    def __init__(self):
        # initialize variables
        self.oldTime = "2023-11-26T19:21:41"
        self.newTime = ""
        self.requestString = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=OLDTIME&endtime=NEWTIME&latitude=32.715736&longitude=-117.161087&maxradiuskm=17'
        self.twitter = Twitter_Handler()

    def run_loop(self):
        # main loop
        while True:
            # Get current time
            current_time = datetime.datetime.now()
            timeString = str(current_time)
            timeString = timeString.replace(' ', 'T')
            timeString = timeString[:-7]

            #variable I want to use
            self.newTime = timeString

            #replace info in requestString
            newRequest = self.requestString.replace('OLDTIME', self.oldTime)
            newRequest = newRequest.replace('NEWTIME', self.newTime)

            #API call
            response = requests.get(newRequest)
            sanDiegoEarthquakes = json.loads(response.text)
            # print(response) #check what the response from the server is, 200 is good

            if (len(sanDiegoEarthquakes['features']) > 0):
                magnitude = sanDiegoEarthquakes['features'][0]['properties']['mag']
                place = sanDiegoEarthquakes['features'][0]['properties']['place']
                timeofEarthquake = sanDiegoEarthquakes['features'][0]['properties']['time']
                date = datetime.datetime.fromtimestamp(timeofEarthquake / 1e3)

                print(newRequest)
                print(response)
                print(str(magnitude) + " magnitude earthquake detected " + str(place) + " on " + str(date)) 
                # THIS IS WHERE I WOULD CALL THE TWITTER FUNCTION AND PASS THE NECESSARY INFORMATION
                self.twitter.sendTweet(str(magnitude) + " magnitude earthquake detected " + str(place) + " on " + str(date))
            else:
                print(newRequest)
                print(response)
                print("No update")

            # update value of oldTime & sleep for 10 seconds before running again
            self.oldTime = self.newTime
            time.sleep(10)
