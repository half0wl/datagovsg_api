datagovsg_api documentation
=========================================

.. toctree::
   :maxdepth: 1

This is an **unofficial** API Wrapper for public APIs at developers.data.gov.sg.
An API key can be obtained from https://developers.data.gov.sg/.

**Disclaimer**: The author is not associated with data.gov.sg, and this
project does not represent data.gov.sg or it's affiliates in any way.

To report bugs or request for features, use the issue tracker on Github
(https://github.com/half0wl/datagovsg_api). For general enquiries or to get
in touch with the author, e-mail: ray <at> half0wl <dot> com.

**Example usage/demo:**

.. code-block:: python

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

.. autoclass:: datagovsg_api.APIClient
    :members:
    :private-members:
