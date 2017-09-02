from sensors.sensor import Sensor
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

class MCP3008(Sensor):
    def __init__(self):
        CLK  = 18
        MISO = 23
        MOSI = 24
        CS   = 25
        self.mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

    def get_data(self):
        return self.mcp.read_adc(1)
