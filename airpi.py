import datetime
from sensors.bmp085 import fuckinBMP085
from sensors.LDR import LDR
from sensors.mics5524 import MICS5524
from sensors.tgs2600 import TGS2600
from sensors.dht22 import fuckinDHT22


class AirPi:
    def __init__(self):
        self.bmp085 = fuckinBMP085()
        self.ldr = LDR()
        self.mics5524 = MICS5524()
        self.tgs2600 = TGS2600()
        self.dht22 = fuckinDHT22()


    def pretty_string(self):
        string = '''
            {}
            Temp: {} *C
            Pressure: {} Pa
            Altitude: {} m
            Sealevel Pressure: {} Pa
            Light Level: {} Ohms
            Volume: {} mV
            Humidity: {}
            Carbon monoxide: {}
            '''
        return string.format(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),
                             self.bmp085.get_data()[0],
                             self.bmp085.get_data()[1],
                             self.bmp085.get_data()[2],
                             self.bmp085.get_data()[3],
                             self.ldr.get_data(),
                             self.tgs2600.get_data(),
                             self.dht22.get_data()[1],
                             self.mics5524.get_data())



