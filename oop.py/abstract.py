from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def milleage(self):
        pass
class Defender(Car):
    def milleage(self):
        print("The milleage of defender is 10km/l")
class Fortuner(Car):
    def milleage(self):
        print("The milleage of fortuner is 12km/l")
class Lancer(Car):
    def milleage(self):
        print("The milleage of lancer is 15km/l")

d=Defender()
f=Fortuner()
l=Lancer()
d.milleage()
f.milleage()
l.milleage()
