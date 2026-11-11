class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __water(self):
        return("{0},{1}".format(self.x,self.y))
    

p1=point(21,20)
print(p1)



        