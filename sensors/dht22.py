from sensors.sensor import Sensor
import Adafruit_DHT


class fuckinDHT22(Sensor):
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = 4

    def get_data(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return ('Temp: {0:0.2f}*C'.format(temperature), '{1:0.2f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
