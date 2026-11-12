from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(animal):
    def move(self):
        print("I SCREAM!!")

class Frog(animal):
    def move(self):
        print("I croak")

class Dog(animal):
    def move(self):
        print("i bark")

class Lion(animal):
    def move(self):
        print("i Roar")

A=Human()
A.move()

B=Frog()
B.move()

C=Dog()
C.move()

D=Lion()
D.move()