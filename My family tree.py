class Familymember:
    def __init__(self,eye_color,height_cm):
        self.eye_color=eye_color
        self.height_cm=height_cm

    def showtraits(self):
        print("My eye color is",self.eye_color)
        print("My height is",self.height_cm)

class child(Familymember):
    def __init__(self, eye_color, height_cm,age,name):
        self.name=name
        self.age=age
        super().__init__(eye_color, height_cm)

    def showtraits(self):
        print("My name is",self.name)
        print("Im",self.age,"years old")
        super().showtraits()

    def favourite_hobby(self,hobby):
        self.hobby=hobby
        print("the favourite hobby is",self.hobby)

Kid=child("brown",150,13,"Nolan")

Kid.showtraits()
Kid.favourite_hobby("Riding my bike")

print("Is child a subclass of Familymember \n",issubclass(child,Familymember))


