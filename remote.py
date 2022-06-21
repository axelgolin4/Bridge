from device import Device


class Remote:
    def __init__(self, device: Device) -> None:
        self.device: Device = device

    def toggle_power(self):
        a = self.device.is_enabled()
        if a == True:
            self.device.enabled()
        else:
            self.device.disable()
            
    def volumen_down(self):
        pass

    def volumen_up(self):
        pass

    def channel_down(self):
        pass

    def channel_up(self):
        pass

