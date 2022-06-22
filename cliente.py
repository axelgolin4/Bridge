from re import T
from remote import Remote
from radio import Radio
from device import Device
from tv import TV
from advanced_remoteP import AdvancedRemoteP

def client(remote: Remote)  -> None:


    print(remote.toggle_power())


if __name__ == "__main__":
   
    
    device = Radio()
    remote = Remote(device)
    print("apagar?")
    client(remote)
    

    print("\n")

    remote = Remote(device)
    print("apagar?")
    client(remote)
    
   