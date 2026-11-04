class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
modelX=vehicle(240,50)
print("These are the details of the vehicle \n Max speed:",modelX.maxspeed)
print("miles taken: ",modelX.mileage)