# datagovsg_api

Unofficial Python API wrapper for public APIs at developers.data.gov.sg.

**Disclaimer**: The author is not associated with data.gov.sg, and this project does not represent data.gov.sg or it's affiliates in any way.

Docs: https://datagovsg_api.readthedocs.io/en/latest/

Example:

```python
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
```

Not yet implemented:

* air_temperature
* pm25
* psi
* rainfall
* relative_humidity
* uv_index
* wind_direction
* wind_speed
