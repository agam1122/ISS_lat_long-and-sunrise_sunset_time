import requests  # Import the requests library to make HTTP requests
from datetime import datetime  # Import datetime to work with dates and times


# Define your latitude and longitude
# Replace 'YOUR_LATITUDE' and 'YOUR_LONGITUDE' with actual values
MY_LAT = 'YOUR_LATITUDE'
MY_LONG = 'YOUR_LONGITUDE'

# Get the current date and time
time_now = datetime.now()


# Define parameters for the API request
# 'lat' and 'lng' are set to your latitude and longitude
# 'date' is set to today's date
# Uncomment the 'formatted' parameter if you want the times in 12-hour format
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "date": time_now.date(),
    # "formatted": 0  # Uncomment to get times in UTC instead of local time
}

# Make a GET request to the Sunrise-Sunset API with the defined parameters
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

# Ensure the request was successful and raise an error if not
response.raise_for_status()

# Parse the JSON response from the API
data = response.json()

# Print the entire response data for inspection (optional)
# print(data)

# Extract sunrise and sunset times from the response
sunrise = data["results"]['sunrise']
sunset = data["results"]['sunset']

# Print the sunrise and sunset times
print(f"Sunrise: {sunrise}, Sunset: {sunset}")

# Print the current date and time for reference
print(time_now.date())
# print(time_now)
