# Weather-script
This is a Python script that uses the OpenWeather API to retrieve current weather information for a specified location. The script first imports the necessary libraries, including requests for making the API call and json for parsing the API response.

The user is prompted to enter their API key and a location, which are then used in the API call URL. The API call is made using the requests.get() method and the response is parsed using json() method.

The script then extracts the relevant information from the API response, such as the temperature, humidity, and weather description, and prints them to the console. The script also includes error handling to catch any exceptions that may occur during the API call or response parsing.

This script can be used as a starting point for building more advanced weather-related applications or for integrating weather information into existing projects. The OpenWeather API offers a wide range of weather data and this script can be easily modified to retrieve and use additional information as needed.
