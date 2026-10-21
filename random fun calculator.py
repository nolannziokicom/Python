print("Welcome to random fun calculator")
print()
print("In this calculator we will improve your math skills by doing the following")
print("1.guess the ceiling and floor of different numbers")
print("2.Try to guess the GCD of different numbers")

import math

enter=float(input("Enter a number with decimals:"))

mathsceil=(math.ceil(enter))
mathsfloor=(math.floor(enter))

print("Ceiling of your number is",mathsceil)
print("the floor of your number is",mathsfloor)

import random
x=random.randint(1,24)
y=random.randint(20,40)

print("x=",x)
print("y=",y)
guess=int(input("Make your guess?(what is the gcd of x and y)"))
answer=("The answer is", math.gcd(x,y))
if guess != answer:
    print("Try again")
else:
    print("Correct the answer is",answer)


