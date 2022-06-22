from device import Device


class SmartTV(Device):

        def __init__(self):
            self.power: bool = False
            self.volumen: int = 0
            self.chanel: float = 0
            self.netflix: bool = False
            self.amazon: bool = False
            self.youtube: bool = False


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

        #funciones especificas de SMART TV.
        def set_Netflix(self, chal):
            self.netflix = True
            self.amazon = False
            self.youtube = False

        def set_Amazon(self, chal):
            self.netflix = False
            self.amazon = True
            self.youtube = False

        def set_Youtube(self, chal):
            self.netflix = False
            self.amazon = False
            self.youtube = True