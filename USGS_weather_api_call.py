import requests
import json
import datetime
import time

########################### TO DO ######################
# Integrate with code to interact with Twitter API
# Call twitter api if True
# Create Proof of concept example to present in the class (time frame where ony 1 incident ocurred, to ensure that the api is called,
# just set oldTime to whatever I need in order for it to show up)

# important links:
# https://earthquake.usgs.gov/fdsnws/event/1/
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

# variables
oldTime = "2023-11-26T19:21:41"
newTime = ""
requestString = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=OLDTIME&endtime=NEWTIME&latitude=32.715736&longitude=-117.161087&maxradiuskm=17'

# main loop
while True:
    # Get current time
    current_time = datetime.datetime.now()
    timeString = str(current_time)
    timeString = timeString.replace(' ', 'T')
    timeString = timeString[:-7]

    #variable I want to use
    newTime = timeString

    #replace info in requestString
    newRequest = requestString.replace('OLDTIME', oldTime)
    newRequest = newRequest.replace('NEWTIME', newTime)

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
    else:
        print(newRequest)
        print(response)
        print("No update")

    # update value of oldTime & sleep for 10 seconds before running again
    oldTime = newTime
    time.sleep(10)
