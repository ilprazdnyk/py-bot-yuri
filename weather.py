import pyowm


def prague_weather():
    owm = pyowm.OWM('f6fefa704d6f1d60ad3c67ae759902e4')
    observation = owm.weather_at_place('Prague, CZ')
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    weather_text = f'The temperature is {temperature}°'
    return weather_text



