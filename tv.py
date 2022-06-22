from device import Device


class TV(Device):

    def __init__(self):
        self.power: bool = False
        self.volumen: int = 0
        self.chanel: float = 0

    def is_enabled(self):
            return self.power
        
    def enabled(self):
            self.power = True
            print("La TV esta: " + self.power)

    def disable(self):
            self.power = False
            print("La TV esta: " + self.power)

    def get_volumen(self):
            return self.volumen
    
    def set_channel(self, chal):
            self.chanel = chal
            print("el Canal es: " + self.chanel)

    def set_volumen(self, vol):
            self.volumen = vol
            print("el Volumen es: " + self.volumen)

    def get_channel(self):
            return self.chanel

    def set_channel(self, chal):
            self.chanel = chal
            print("el Canal es: " + self.chanel)
    
    #funciones especificas de TV.
