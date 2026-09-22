import random
random1=int (random.randint(1,30))
attempt=0
   
while attempt <= 5:
      attempt=int(input("please input your attempts here "))
      
      if random1 == attempt:
        
        print("congratulations you won")
      elif random1 != attempt:
        print("Wrong guess try again ")
        if attempt > random1:
            print("ice cold")
            print("Too high aim lower")
        else:
            print("Hotttt!")
            print("too low aim higher")
      else:
        print("Invaliid input please enter a normal number")








