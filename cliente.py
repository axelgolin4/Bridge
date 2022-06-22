from remote import Remote
from radio import Radio
from device import Device
from tv import TV
from smart_tv import SmartTV
from advanced_remoteA import AdvancedRemoteA
from advanced_remoteP import AdvancedRemoteP
import os


def client(remote: Remote, dis)  -> None:
    if dis=="1":
        Salir = 0
        while( Salir != 1):
            print("1. Encender")
            print("2. Apagar")
            print("3. Cambiar Canal")
            print("4. Subir Canal")
            print("5. Bajar Canal")
            print("6. Subir volumen")
            print("7. Bajar volumen")
            print("8. Salir")

            opcionMenu = input("inserta un numero valor >> ")
            if opcionMenu=="1":
                remote.toggle_power()
            elif opcionMenu=="2":
                remote.toggle_power()
            elif opcionMenu=="3":
                remote.set_channel(input("numero de canal: "))
            elif opcionMenu=="4":
                remote.channel_up()
            elif opcionMenu=="5":
                remote.channel_down()
            elif opcionMenu=="6":
                remote.volumen_up()
            elif opcionMenu=="7":
                remote.volumen_down    
            elif opcionMenu=="8":
                Salir=1
                
    elif dis=="2":
        Salir = 0
        while( Salir != 1):
            print("1. Encender")
            print("2. Apagar")
            print("3. Cambiar Canal")
            print("4. Subir Canal")
            print("5. Bajar Canal")
            print("6. Subir volumen")
            print("7. Bajar volumen")
            print("8. Salir")

            opcionMenu = input("inserta un numero valor >> ")
            if opcionMenu=="1":
                remote.toggle_power()
            elif opcionMenu=="2":
                remote.toggle_power()
            elif opcionMenu=="3":
                remote.set_channel(input("numero de canal: "))
            elif opcionMenu=="4":
                remote.channel_up()
            elif opcionMenu=="5":
                remote.channel_down()
            elif opcionMenu=="6":
                remote.volumen_up()
            elif opcionMenu=="7":
                remote.volumen_down    
            elif opcionMenu=="8":
                Salir=1

    elif dis=="3":
        Salir = 0
        while( Salir != 1):
            print("1. Netflix")
            print("2. Amazon")
            print("3. Youtube")
            print("4. Subir volumen")
            print("5. Bajar volumen")
            print("6. Salir")

            opcionMenu = input("inserta un numero valor >> ")
    
            if opcionMenu=="1":
                print("-------------------Netflix--------------------------------")
                print(remote.open_netflix())
            elif opcionMenu=="2":
                print("-------------------AMAZON--------------------------------")
                print(remote.open_amazon())
            elif opcionMenu=="3":
                print("-------------------Youtube--------------------------------")
                print(remote.open_youtube())
            elif opcionMenu=="4":
                remote.volumen_up()
            elif opcionMenu=="5":
                remote.volumen_down()
            elif opcionMenu=="6":
                Salir=1
        


 
 



if __name__ == "__main__":

    print("bienvenidos")
    print("Radio")
    print("Television")
    print("Smart TV")

    dis = input("elija un Dispositivo: ")
    
    if dis=="1":
        device = Radio()
    elif dis=="2":
        device = TV()
    elif dis=="3":
        device = SmartTV()
    
    
    
    
    
    print("Control A (Control funcinal)")
    print("Control P (mas inteligente)")

    control = input("elija un control: ")
    
    if control=="1":
        remote = AdvancedRemoteA(device)
    elif control=="2":
        remote = AdvancedRemoteP(device)
    
    
    
    client(remote,dis)
    

    print("\n")
    
   