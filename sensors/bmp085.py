from sensors.sensor import Sensor
import Adafruit_BMP.BMP085 as BMP085


class fuckinBMP085(Sensor):
	def __init__(self):
		self.sensor = BMP085.BMP085()

	def get_data(self):
		return ('{0:0.2f}'.format(self.sensor.read_temperature()),
		'{0:0.2f}'.format(self.sensor.read_pressure()),
		'{0:0.2f}'.format(self.sensor.read_altitude()),
		'{0:0.2f}'.format(self.sensor.read_sealevel_pressure()))
