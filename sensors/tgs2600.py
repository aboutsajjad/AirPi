from sensors.mcp3008 import MCP3008

class TGS2600(MCP3008):
    
    def get_data(self):
        pullDown = 22000
        result = self.mcp.read_adc(4)
        vin = 3.3
        vout = float(result)/1023 * vin
        resOut = (pullDown*vin)/vout - pullDown
        return resOut
