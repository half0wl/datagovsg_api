import datagovsg_api

datagovsg = datagovsg_api.APIClient(API_KEY='your_api_key')

# get taxi availability
taxi_availability = datagovsg.taxi_availability()
assert taxi_availability.status_code == 200  # ensure response is 200 OK
print(taxi_availability.json())  # print the json response

datagovsg.taxi_availability(date_time='2016-12-12T09:45:00').json()  # for data at specific date/time

# get traffic images
datagovsg.traffic_images().json()  # latest
datagovsg.traffic_images(date_time='2016-12-12T09:45:00').json()  # for data at specific date/time

# get weather forecast
datagovsg.weather_forecast(duration='2-hour').json()
datagovsg.weather_forecast(duration='24-hour').json()
datagovsg.weather_forecast(duration='4-day').json()
