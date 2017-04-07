import datagovsg_api

datagovsg = datagovsg_api.APIClient(API_KEY='your_api_key')

# get taxi availability
datagovsg.taxi_availability()  # latest
datagovsg.taxi_availability(date_time='2016-12-12T09:45:00')  # for data at specific date/time

# get traffic images
datagovsg.traffic_images()  # latest
datagovsg.traffic_images(date_time='2016-12-12T09:45:00')  # for data at specific date/time

# get weather forecast
datagovsg.weather_forecast(duration='2-hour')
datagovsg.weather_forecast(duration='24-hour')
datagovsg.weather_forecast(duration='4-day')
