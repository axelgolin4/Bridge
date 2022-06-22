from device import Device


class Radio(Device):
    
    def __init__(self):
        self.power: bool = False
        self.volumen: int = 0
        self.chanel: float = 0


    def is_enabled(self):
        return self.power

    def enabled(self):
        self.power = True

    def disable(self):
        self.power = False

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, vol):
        self.volumen = vol

    def get_channel(self):
        return self.chanel

    def set_channel(self, chal):
        self.chanel = chal
