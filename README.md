# datagovsg_api

[![Build Status](https://travis-ci.org/half0wl/datagovsg_api.svg?branch=master)](https://travis-ci.org/half0wl/datagovsg_api) [![Documentation Status](https://readthedocs.org/projects/datagovsg-api/badge/?version=latest)](http://datagovsg-api.readthedocs.io/en/latest/?badge=latest)

Unofficial Python API wrapper for public APIs at [developers.data.gov.sg](https://developers.data.gov.sg/). An API key is required and can be obtained from [https://developers.data.gov.sg/](https://developers.data.gov.sg/).

**Disclaimer**: The author is not associated with data.gov.sg, and this project does not represent data.gov.sg or it's affiliates in any way.

## Installation

`$ pip install datagovsg_api`

## Usage

**API Reference**: https://datagovsg_api.readthedocs.io/en/latest/

The `TransportAPI` class provides an interface to APIs under the Transport category.

```python
import datagovsg_api

sg_transport = datagovsg_api.TransportAPI('API_KEY')

# Get taxi availability
print(sg_transport.taxi_availability().json())
```

The `EnvironmentAPI` class provides an interface to APIs under the Environment category.

```python
import datagovsg_api

sg_environment = datagovsg_api.EnvironmentAPI('API_KEY')

# Get 2-hour weather forecast
print(sg_environment.weather_forecast('2-hour').json())

# Get the PSI readings at a particular moment in time
datetime_to_retrieve = '2016-12-12T09:45:00'
print(sg_environment.psi(date_time=datetime_to_retrieve).json())

# Get the wind direction on a particular date
date_to_retrieve = '2016-12-12'
print(sg_environment.wind_direction(date=date_to_retrieve).json())
```

If you need access to both Transport and Environment APIs, there's an `AllAPI` class.

```python
import datagovsg_api

sg_data = datagovsg_api.AllAPI('API_KEY')

# Get taxi availability
print(sg_data.taxi_availability().json())

# Get 2-hour weather forecast
print(sg_data.weather_forecast(duration='2-hour').json())
```

All methods return a `Response` object. Call `.json()` to retrieve the
data.

```python
>>> import datagovsg_api
>>> sg_transport = datagovsg_api.TransportAPI('API_KEY')
>>> taxi_availability = sg_transport.taxi_availability()
>>> type(taxi_availability)
<class 'requests.models.Response'>
>>> taxi_availability.status_code
200
>>> taxi_availability.json()
{'type': 'FeatureCollection', 'crs': {'type': 'link', 'properties': {'href': 'http://spatialreference.org/ref/epsg/4326/ogcwkt/', 'type': 'ogcwkt'}}, 'features': [{'type': 'Feature', 'geometry': {'type': 'MultiPoint', 'coordinates': [[103.61401, 1.25224], [103.6218, 1.274137], [103.62295, 1.28297], [103.6232, 1.29934], [103.62367, 1.30091], [103.62471, 1.30781], [103.62622, 1.28103], [103.6265, 1.29537], [103.62748, 1.28803], [103.62778, 1.28701], [103.62859, 1.31048], [103.62898, 1.31463], [103.62996, 1.28483], [103.63304, 1.31035], [103.63497, 1.32925], [103.63846, 1.33281], [103.64054, 1.32225], [103.64115, 1.31938], [103.64326, 1.33401], [103.64734, 1.31784], [103.64799, 1.32955], ... [truncated]
```

Most methods have an optional `date` and/or `date_time` parameter which
can be used to retrieve the latest available data at that particular moment.
The format for `date` is `YYYY-MM-DD` (e.g. `2016-12-12`). The format
for `date_time` is `YYYY-MM-DD[T]HH:mm:ss (SGT)` (e.g. `2016-12-12T09:45:00`).

```python
>>> import datagovsg_api
>>> sg_environment = datagovsg_api.EnvironmentAPI('API_KEY')
>>> sg_environment.psi(date='2016-12-12').json()
{'region_metadata': [{'name': 'national', 'label_location': {'longitude': 0, 'latitude': 0}}, {'name': 'south', 'label_location': {'longitude': 103.82, 'latitude': 1.29587}}, {'name': 'north', 'label_location': {'longitude': 103.82, 'latitude': 1.41803}}, {'name': 'east', 'label_location': {'longitude': 103.94, 'latitude': 1.35735}}, {'name': 'central', 'label_location': {'longitude': 103.82, 'latitude': 1.35735}}, {'name': 'west', 'label_location': {'longitude': 103.7, 'latitude': 1.35735}}], 'items': [{'timestamp': '2016-12-12T01:00:00+08:00', ... [truncated]
>>> sg_environment.psi(date_time='2016-12-12T09:45:00').json()
{'region_metadata': [{'name': 'national', 'label_location': {'longitude': 0, 'latitude': 0}}, {'name': 'south', 'label_location': {'longitude': 103.82, 'latitude': 1.29587}}, {'name': 'north', 'label_location': {'longitude': 103.82, 'latitude': 1.41803}}, {'name': 'east', 'label_location': {'longitude': 103.94, 'latitude': 1.35735}}, {'name': 'central', 'label_location': {'longitude': 103.82, 'latitude': 1.35735}}, {'name': 'west', 'label_location': {'longitude': 103.7, 'latitude': 1.35735}}], 'items': [{'timestamp': '2016-12-12T09:00:00+08:00', ... [truncated]
```

## List of available methods

Click on the hyperlink icon 🔗 for the method's API reference on [readthedocs](https://datagovsg-api.readthedocs.io/en/latest/).

**TransportAPI** [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.TransportAPI)

* `taxi_availability()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.TransportAPI.taxi_availability)
* `traffic_images()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.TransportAPI.traffic_images)

**EnvironmentAPI**  [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI)

* `weather_forecast()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.weather_forecast)
* `air_temperature()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.air_temperature)
* `pm25()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.pm25)
* `psi()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.psi)
* `rainfall()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.rainfall)
* `relative_humidity()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.relative_humidity)
* `uv_index()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.uv_index)
* `wind_direction()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.wind_direction)
* `wind_speed()` [🔗](https://datagovsg-api.readthedocs.io/en/latest/#datagovsg_api.EnvironmentAPI.wind_speed)
