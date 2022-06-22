from remote import Remote


class AdvancedRemoteA(Remote):
    
    def toggle_power(self):
        a = self.device.is_enabled()
        if a == True:
            self.device.enabled()
            return self.device.is_enabled()
        else:
            self.device.disable()
            return self.device.is_enabled()
            
    def volumen_down(self):
        a = self.device.get_volumen()
        a = a - 1
        self.device.set_volumen(a)

    def volumen_up(self):
        a = self.device.get_volumen()
        a = a + 1
        self.device.set_volumen(a)

    def channel_down(self):
        a = self.device.get_volumen()
        a = a - 1
        self.device.set_volumen(a)

    def channel_up(self):
        a = self.device.get_volumen()
        a = a + 1
        self.device.set_volumen(a)
    
    
    def mute(self):
        self.device.set_volumen(0)

    def change_channel(self, channel):
        self.device.set_channel(channel)

    def change_volumen(self, volumen):
        self.device.set_volumen(volumen)

