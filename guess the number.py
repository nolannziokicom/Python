import random
play=True
n= str (random.randint(0,9))
print("Guess the number 0-9")
while play:
   guess=input("Please input your number here")
   if guess == n:
    print("Congartulations for guessing the number")
    break
   else:
    print("Try again")




