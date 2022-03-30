from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



def OWMMOD1(x):
    owm = OWM('b0c99ce5cec673f9bf605ca8f8b39323')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(x+', RU')
    w = observation.weather

    a = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    return a['temp']

def OWMMOD2(x):
        owm = OWM('b0c99ce5cec673f9bf605ca8f8b39323')
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(x+', RU')
        w = observation.weather

        a = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        return a['temp_max']


def OWMMOD3(x):
    owm = OWM('b0c99ce5cec673f9bf605ca8f8b39323')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(x+', RU')
    w = observation.weather

    a = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    return a['temp_min']

#Вывод всех температур
def OWMMOD(x):
    owm = OWM('b0c99ce5cec673f9bf605ca8f8b39323')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(x+', RU')
    w = observation.weather

    a = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print(a)