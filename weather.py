import pyowm


def prague_weather():
    owm = pyowm.OWM('*Code from OpenWeatherMap')
    observation = owm.weather_at_place('Prague, CZ')
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    cloud_coverage = weather.get_clouds()
    weather_status = weather.get_detailed_status()
    weather_text = f'The weather status is: {weather_status} \nThe temperature is {temperature}° ' \
                   f'\nThe cloud coverage is {cloud_coverage}%'
    return weather_text





