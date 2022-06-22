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
            print("La TV esta: " + self.power)

        def disable(self):
            self.power = False
            print("La TV esta: " + self.power)

        def get_volumen(self):
            return self.volumen

        def set_volumen(self, vol):
            self.volumen = vol
            print("el Volumen es: " + self.volumen)

        def get_channel(self):
            return self.chanel

        #funciones especificas de SMART TV.
        def set_Netflix(self):
            self.netflix = True
            self.amazon = False
            self.youtube = False
            print(" ")
            print("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌     ")
            print("───▄▄██▌█ BEEP BEEP          ")
            print("▄▄▄▌▐██▌█                    ")
            print("███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌     ")
            print("▀(@)▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀(@)▀   ")
            


        def set_Amazon(self):
            self.netflix = False
            self.amazon = True
            self.youtube = False
            print(" ")
            print("          ═══•◉•═════        ")
            print("          ▂▄▄▓▄▄▂           ")
            print("       ◢◤ █▀▀████▄▄▄▄◢◤     ")
            print("       █▄ █ █▄ ███▀▀▀▀▀▀▀╬    ")
            print("       ◥█████◤               ")
            print("         ═╩══╩═               ")

        def set_Youtube(self):
            self.netflix = False
            self.amazon = False
            self.youtube = True
            print(" ")
            print(" ╭━━━━-╮ ")
            print(" ╰┃ ┣▇━▇ ")
            print("   ┃ ┃  ╰━▅╮")
            print("  ╰┳╯ ╰━━┳╯")
            print("   ╰╮ ┳━━╯")
            print("  ▕▔▋ ╰╮╭━╮")
            print("╱▔╲▋╰━┻┻╮╲╱▔▔▔╲ ")
            print("▏  ▔▔▔▔▔▔▔  O O┃ ")
            print("╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱ ")
            print(" ▏╳▕▇▇▕ ▏╳▕▇▇▕ ")
            print("╲▂╱╲▂╱ ╲▂╱╲▂╱ ")
           

