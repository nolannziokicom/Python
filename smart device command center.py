from abc import ABC,abstractmethod

class device(ABC):
    def devicetype(self,name):
        self.name=name
        print("device name: ", self.name)

    @abstractmethod
    def turnon(self):
        print("This is for turning the device on or off")

class smartlight(device):
    def turnon(self):
        print("light is now on")

class speaker(device):
    def turnon(self):
        print("bluetooth device is ready to pair. speaker on")



light=smartlight()
dat=speaker()

light.devicetype("a bulb")
light.turnon()
dat.devicetype("a speaker")
dat.turnon()
