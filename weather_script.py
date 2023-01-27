import requests
from datetime import datetime

def get_weather(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&" + location
    response = requests.get(complete_url)
    return response.json()

def get_forecast(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "appid=" + api_key + "&" + location
    response = requests.get(complete_url)
    return response.json()

def display_weather(weather_data, units):
    # Extracting the required information
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    weather_description = weather_data['weather'][0]['description']
    city_name = weather_data['name']
    country_code = weather_data['sys']['country']

    if units.lower() == "celsius" or units.lower() == "c":
        temperature_in_selected_unit = temperature - 273.15
        unit_symbol = "°C"
    elif units.lower() == "fahrenheit" or units.lower() == "f":
        temperature_in_selected_unit = (temperature - 273.15) * 9/5 + 32
        unit_symbol = "°F"
    else:
        raise ValueError("Invalid units. Please specify 'celsius' or 'fahrenheit'.")

    # Displaying the extracted information
    print(f"Weather in {city_name}, {country_code}:")
    print(f"Temperature: {temperature_in_selected_unit:.2f}{unit_symbol}")
    print(f"Humidity: {humidity}%")
    print(f"Forecast: {weather_description}")

def display_forecast(forecast_data, units):
    forecast_list = forecast_data['list']
    print("Date\t\t\tTemperature\tHumidity\tForecast")
    for forecast in forecast_list:
        date_time = datetime.fromtimestamp(forecast['dt'])
        date = date_time.strftime("%Y-%m-%d %H:%M:%S")
        if units.lower() == "celsius" or units.lower() == "c":
            temperature_in_selected_unit = forecast['main']['temp'] - 273.15
            unit_symbol = "°C"
        elif units.lower() == "fahrenheit" or units.lower() == "f":
            temperature_in_selected_unit = (forecast['main']['temp'] - 273.15) * 9/5 + 32
            unit_symbol = "°F"
        else:
            raise ValueError("Invalid units. Please specify 'celsius' or 'fahrenheit'.")
        humidity = forecast['main']['humidity']
        weather_description = forecast['weather'][0]['description']
        print(f"{date}\t{temperature_in_selected_unit:.2f}{unit_symbol}\t\t{humidity}%\t\t{weather_description}")

def save_to_file(data, file_name, units):
    with open(file_name, 'w') as f:
        for forecast in data['list']:
            date_time = datetime.fromtimestamp(forecast['dt'])
            date = date_time.strftime("%Y-%m-%d %H:%M:%S")
            if units.lower() == "celsius":
                temperature_in_selected_unit = forecast['main']['temp'] - 273.15
                unit_symbol = "°C"
            elif units.lower() == "fahrenheit":
                temperature_in_selected_unit = (forecast['main']['temp'] - 273.15) * 9/5 + 32
                unit_symbol = "°F"
            else:
                raise ValueError("Invalid units. Please specify 'celsius' or 'fahrenheit'.")
            humidity = forecast['main']['humidity']
            weather_description = forecast['weather'][0]['description']
            f.write(f"{date}\t{temperature_in_selected_unit:.2f}{unit_symbol}\t\t{humidity}%\t\t{weather_description}\n")

def save_to_file(data, file_name, units):
    with open(file_name, 'w') as f:
        if 'list' in data: # check if the data is forecast data
            for forecast in data['list']:
                date_time = datetime.fromtimestamp(forecast['dt'])
                date = date_time.strftime("%Y-%m-%d %H:%M:%S")
                if units.lower() == "celsius" or units.lower() == "c":
                    temperature_in_selected_unit = forecast['main']['temp'] - 273.15
                    unit_symbol = "°C"
                elif units.lower() == "fahrenheit" or units.lower() == "f":
                    temperature_in_selected_unit = (forecast['main']['temp'] - 273.15) * 9/5 + 32
                    unit_symbol = "°F"
                else:
                    raise ValueError("Invalid units. Please specify 'celsius' or 'fahrenheit'.")
                humidity = forecast['main']['humidity']
                weather_description = forecast['weather'][0]['description']
                f.write(f"{date}\t{temperature_in_selected_unit:.2f}{unit_symbol}\t\t{humidity}%\t\t{weather_description}\n")
        else: # it is weather data
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_description = data['weather'][0]['description']
            city_name = data['name']
            country_code = data['sys']['country']

            if units.lower() == "celsius" or units.lower() == "c":
                temperature_in_selected_unit = temperature - 273.15
                unit_symbol = "°C"
            elif units.lower() == "fahrenheit" or units.lower() == "f":
                temperature_in_selected_unit = (temperature - 273.15) * 9/5 + 32
                unit_symbol = "°F"
            else:
                raise ValueError("Invalid units. Please specify 'celsius' or 'fahrenheit'.")
                
            f.write(f"Weather in {city_name}, {country_code}:\n")
            f.write(f"Temperature: {temperature_in_selected_unit:.2f}{unit_symbol}\n")
            f.write(f"Humidity: {humidity}%\n")
            f.write(f"Forecast: {weather_description}\n")



api_key = "c041b76f1d1508338f0e940f153b9ff9"
print()
location_input = input("Enter the location: ").capitalize()
location = "q=" + location_input
celcius_or_farenheit = input("Celcius or Farenheit: ").lower()
weather_data = get_weather(location, api_key)
print()
display_weather(weather_data, celcius_or_farenheit)
########################################################################################
forecast_choice = input(f"\nWould you like the forecast in {location_input}?(Y/N): ")
x = ""
if forecast_choice.lower() == "y" or forecast_choice.lower() == "yes":
    forecast_data = get_forecast(location, api_key)
    display_forecast(forecast_data, "c")
    x = "and forecast "
#########################################################################################
save_to_file_choice = input(f"\nWould you like to save the weather {x}data of {location_input}?(Y/N): ")
if save_to_file_choice.lower() == 'y' or save_to_file_choice.lower() == 'yes':
    save_to_file(weather_data, 'weather.txt', celcius_or_farenheit)
    if forecast_choice.lower() == "y" or forecast_choice.lower() == "yes":
        save_to_file(forecast_data, 'forecast.txt', celcius_or_farenheit)
