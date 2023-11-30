from USGS_weather_api_call import USGS_weather_api_call

if __name__ == '__main__':
    weather_api = USGS_weather_api_call()
    weather_api.run_loop()