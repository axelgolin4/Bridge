from device import Device


class Remote:
    def __init__(self, device: Device) -> None:
        self.device: Device = device

    def toggle_power(self):
        raise NotImplementedError
            
    def volumen_down(self):
        raise NotImplementedError

    def volumen_up(self):
        raise NotImplementedError

    def channel_down(self):
       raise NotImplementedError

    def channel_up(self):
        raise NotImplementedError

    

