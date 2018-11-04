### given more time, error handleing should be thought thorough and implemented

import json
import requests
from pycountry_convert import country_alpha2_to_country_name


## part 1

my_ip_and_location = requests.get("https://ifconfig.co/json").json()
latitude = my_ip_and_location["latitude"]
longitude = my_ip_and_location["longitude"]
weather_api_url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=dec07a75427862501fb3e97181ac04e8&units=metric".format(latitude, longitude)
weather_api_call = requests.get(weather_api_url).json()
temperture = weather_api_call["main"]["temp"]
weather_var = open("weather_file.txt", "w")
weather_var.write(str(temperture))


## part 2

#takes a city name and returns and array of temperture and country code
def what_temperture_and_country_code(city):
    fixed_city_name = city.replace(" ","+").replace("-","+")
    f_weather_api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=dec07a75427862501fb3e97181ac04e8&units=metric".format(fixed_city_name)
    f_weather_api_call = requests.get(f_weather_api_url).json()
    f_temperture = f_weather_api_call["main"]["temp"]
    f_country_code = f_weather_api_call["sys"]["country"]
    findings_array = [f_temperture,f_country_code]
    return findings_array

# main section - prints as asked, some of the country code provided from open weather are not correct and it is not handled in the program
cities = ["Seoul","Tokyo","Tel-Aviv","Kuala Lumpur","Singapore","New York","Dubai","Paris","London","Bangkok"]
temperture_country_code_array = []
cities_index = 0
for i in cities:
     temp_array = what_temperture_and_country_code(i)
     temperture_country_code_array.append(temp_array)
     full_country_name = country_alpha2_to_country_name(temperture_country_code_array[cities_index][1])
     temperture_of_city = temperture_country_code_array[cities_index][0]
     print("the weather in city",i,full_country_name,"is",temperture_of_city,"degrees")
     cities_index = cities_index + 1

