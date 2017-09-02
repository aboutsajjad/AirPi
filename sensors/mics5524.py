from sensors.mcp3008 import MCP3008

class MICS5524(MCP3008):
    
    def get_data(self):
        return self.mcp.read_adc(1)
