from device import Device


class TV(Device):

    def __init__(self):
        self.power: bool = False

    def is_enabled(self):
        return self.power

    def enabled(self):
        self.power = True

    def disable(self):
        self.power = False

    def get_volumen(self):
        pass

    def set_volumen(self):
        pass

    def get_channel(self):
        pass

    def set_channel(self):
        pass
