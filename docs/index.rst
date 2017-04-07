datagovsg_api documentation
=========================================

.. toctree::
   :maxdepth: 1

This is an **unofficial** API Wrapper for public APIs at developers.data.gov.sg.
An API key can be obtained from https://developers.data.gov.sg/.

**Disclaimer**: The author is not associated with data.gov.sg, and this
project does not represent data.gov.sg or it's affiliates in any way.

To report bugs or request for features, use the issue tracker on Github
(`@half0wl/datagovsg_api <https://github.com/half0wl/datagovsg_api/>`_).

For general enquiries or to get in touch with the author, e-mail: ray
<at> half0wl <dot> com.

**Example usage/demo:**

.. code-block:: python

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

.. autoclass:: datagovsg_api.APIClient
    :members:
    :private-members:
