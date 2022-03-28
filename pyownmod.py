from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
def OWMMOD():
    owm = OWM('b0c99ce5cec673f9bf605ca8f8b39323')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Kirov,RU')
    w = observation.weather

    a = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print(a)
    print(a['temp'])
    print(a['temp_max'])
    print(a['temp_min'])