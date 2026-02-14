import requests  
# Library used to send HTTP requests to the API
# ==============================
# IMPORTANT:
# Replace the API key below with your own API key
# API key from OpenWeatherMap website
# ==============================

API_KEY = "00e25dcb505e1df8dc23d7a4c60365b7"


def get_weather(city_name):
    """
    This function takes a city name as input,
    sends a request to the OpenWeatherMap API,
    and prints the weather details.
    """

    # API endpoint URL with parameters:
    # q = city name
    # appid = API key
    # units = metric (for temperature in Celsius)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    try:
        # Send GET request to the API
        response = requests.get(url)

        # Convert response data into JSON format
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:

            # Extract important information from JSON data
            city = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            # Display formatted weather information
            print("\n==========🌍 Weather Report ==========")
            print(f"City: {city}, {country}")
            print(f"Temperature: {temperature}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {description.capitalize()}")
            print("====================================")

        else:
            # If city is not found or API key is wrong
            print("\nSorry, I couldn't find city. Is the spelling correct?")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print("Network error occurred:", e)


# ==============================
# Main Program Starts Here
# ==============================

# Take city name input from user
city_input = input("Enter City Name: ")

# Call the function to get weather data
get_weather(city_input)
