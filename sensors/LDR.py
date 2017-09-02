from sensors.mcp3008 import MCP3008

class LDR(MCP3008):

    def get_data(self):
        pullUp = 10000
        result = self.mcp.read_adc(0)
        vin = 3.3
        vout = float(result)/1023 * vin
        resOut = pullUp/((vin/vout)-1)
        return self.mcp.read_adc(0)
