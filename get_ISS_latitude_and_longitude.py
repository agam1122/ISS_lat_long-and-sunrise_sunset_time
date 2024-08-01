import requests  # Import the requests library to make HTTP requests

# Send a GET request to the ISS (International Space Station) API to get its current location
response = requests.get(url='http://api.open-notify.org/iss-now.json')

# Check if the response status code is not 200 (HTTP OK)
# This indicates that something went wrong with the API request
if response.status_code != 200:
    # Raise an exception with a custom message if the status code is not OK
    raise Exception("Bad response from ISS API")

# Ensure that the HTTP response status is 200 (OK) and raise an error for any HTTP errors
response.raise_for_status()

# Parse the JSON response to extract the ISS position data
data = response.json()["iss_position"]

# Print the ISS position data, which includes latitude and longitude
print(data)



