class car:
    def __init__(self,color,size):
        self.size=size
        self.color=color

    def showdetails(self):
        print("The car is",self.color,"color")
        print("The car is",self.size,"kg heavy,")

class details(car):
    def __init__(self, color, size,type,miles):
        self.type=type
        self.miles=miles
        
        super().__init__(color, size)

    def showdetails(self):
        print("The car is a",self.type)
        print("The car has gone",self.miles,"miles")
        super().showdetails()

detail=details("carbon fiber black",1516,"porsche",100)
detail.showdetails()

