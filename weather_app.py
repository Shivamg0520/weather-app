import requests
city_name = str(input("Enter city name: "))
def fetch_weather_data(city):
    api_key = "API-KEY"  # Replace with your actual API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        city = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        time_zone = data['location']['tz_id']
        local_time = data['location']['localtime']
        temp_in_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        wind_speed = data['current']['wind_kph']
        humidity = data['current']['humidity']
        feel_temp = data['current']['feelslike_c']
        return city, region, country, time_zone, local_time, temp_in_c, condition, wind_speed, humidity, feel_temp
    else:
        raise Exception("Failed to fetch data")
def main():
    try:
        city, region, country, time_zone, local_time, temp_in_c, condition, wind_speed, humidity, feel_temp = fetch_weather_data(city_name)
        print(f"City: {city}\nRegion: {region}\nCountry: {country}\nTime Zone: {time_zone}\nLocal Time: {local_time}\nTemperature (C): {temp_in_c}\nCondition: {condition}\nWind Speed (kph): {wind_speed}\nHumidity: {humidity}\nFeels Like (C): {feel_temp}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
