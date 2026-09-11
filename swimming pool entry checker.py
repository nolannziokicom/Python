print("Welcome to the swimming pool entry checker ")
print()

age=input("What is your age range(toddler,teen or adult")
adult_here=input("Do you have an adult with you?(yes/no)")
deepeend=input("Can you swim in the deep end without drowning")

if age=="toddler" and adult_here=="no" and deepeend=="no":
    print("YOU ARE NOT ALLOWED INTO THE SWIMMING POOL!")
elif age=="toddler" and adult_here=="yes":
    print("You can go into the shallow end with the adult")


if age=="teen" and adult_here=="no" and deepeend=="no":
    print("Swim with caution and ensure you dont go into the deep end")
elif age=="teen" and adult_here=="yes" and deepeend=="yes":
    print("you can swim freely anywhere in the swimming pool")
elif age=="teen" and adult_here=="no" and deepeend=="yes":
    print("Ensure you swim with caution and focus to ensure you dont drown as there isnt an adult")
  
if age=="adult" and adult_here=="yes" and deepeend=="yes":
    print("You can swim freely however you want")
elif age=="adult" and adult_here=="no"and deepeend=="yes":
    print("You can swim freely but with a little bit of caution")
elif age=="adult" and adult_here=="no"and deepeend=="no":
    print("Swim with caution and try to swim near the shallow end")


