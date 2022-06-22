from remote import Remote


class AdvancedRemoteP(Remote):

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

    def open_netflix(self):
        self.device.set_Netflix()
            
    def open_amazon(self):
        self.device.set_Amazon()

    def open_youtube(self):
        self.device.set_Youtube()

