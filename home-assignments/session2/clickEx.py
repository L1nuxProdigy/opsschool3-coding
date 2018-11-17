import subprocess
import sys

try:
    import click
    import weather
except ModuleNotFoundError:
    subprocess.call(['pip3', 'install', 'click'])
    subprocess.call(['pip3', 'install', 'weather-api'])
import click
from weather import Weather, Unit


@click.command()
@click.option('--city', default="Error", help='The Desired City')
@click.option('--forecast', default="TODAY", help='day/s of forecast')
@click.option('-c/-f', default=True, help='temperature in celsius or fahrenheit')


def main(city, forecast, c):
    check_forecast_input(forecast)
    temperature_metric, weather = what_temperature_metric(c)
    location, condition = check_valid_location(city, weather)
    if forecast == "TODAY":
        output_for_single_day(city,location,condition,temperature_metric)
    else:
        output_for_single_day(city, location, condition, temperature_metric)
        output_for_multiple_days(forecast, location, temperature_metric)



def check_forecast_input(forecast):
    if forecast[:5] != "TODAY":
        print("Input incorrect!, forecast parameter should start with TODAY")
        sys.exit()
    if len(forecast) == 6 and forecast[5] != "+":
        print(
            "Input incorrect!, forecast parameter should start with TODAY, TODAY+int can be used to receive upcoming forecasts")
        sys.exit()
    if len(forecast) <= 5:
        return
    else:
        try:
            if int(forecast[6:]) <= 0 or int(forecast[6:]) >= 10:
                print("Input incorrect!, the forecasts available are up to 9 days from today")
                sys.exit()
        except ValueError:
            print("dude stop trying to mess with the program and enter somthing valid")
            sys.exit()


def weather_in_fahrenheit():
    weather = Weather(unit=Unit.FAHRENHEIT)
    return weather


def weather_in_celsius():
    weather = Weather(unit=Unit.CELSIUS)
    return weather


def what_temperature_metric(c):
    if c:
        weather = weather_in_celsius()
        temperature_metric = "celsius"
    else:
        weather = weather_in_fahrenheit()
        temperature_metric = "fahrenheit"
    return temperature_metric, weather


def check_valid_location(city, weather):
    location = weather.lookup_by_location(city)
    try:
        condition = location.condition
    except AttributeError:
        print("provide a valid city name, {} does not exist in the database".format(city))
        sys.exit()
    return location, condition


def output_for_single_day(city,location,condition,temperature_metric):
    forecasts = location.forecast
    low_temperature = forecasts[0].low
    high_temperature = forecasts[0].high
    print("The Weather in {} today is {} with temperatures trailing from {}-{} {}".format(city, condition.text,
                                                                                          low_temperature,
                                                                                          high_temperature,
                                                                                          temperature_metric))


def output_for_multiple_days(forecast, location, temperature_metric):
    days_after = forecast[-1]
    forecasts = location.forecast
    print("forecast for the next {} days".format(days_after))
    for forecast_index in range(1, int(days_after) + 1):
        location_overview = forecasts[forecast_index].text
        date = forecasts[forecast_index].date
        low_temperature = forecasts[forecast_index].low
        high_temperature = forecasts[forecast_index].high
        print("{} {} with temperatures trailing from {}-{} {}.".format(date, location_overview, low_temperature,
                                                                       high_temperature, temperature_metric))


if __name__ == "__main__":
    main()