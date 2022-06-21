from device import Device


class Remote:
    def __init__(self, device: Device) -> None:
        self.__device: Device = device

    def toggle_power(self):
        if self.__device.is_enabled() == True:
            self.__device.disable()
        elif:



    def volumen_down(self):
        pass

    def volumen_up(self):
        pass

    def channel_down(self):
        pass

    def channel_up(self):
        pass

