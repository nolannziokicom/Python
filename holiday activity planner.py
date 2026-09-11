print("holiday activity planner")
print("Answer these three questions and i'll plan your day \n")



day = input("What day is it?").strip().capitalize()
weather= input("What is the weather today: (Sunny/rainy/cloudy)").strip().lower()
homework =input("Have you finished your homework?").strip().lower()

print("")

print("-"* 35)

if day in ("Saturday","Sunday"):
   print("Enjoy your weekend by going to the park")
elif day == "Monday":
   print("You can bike ride to start the week of strong")
elif day =="Friday":
   print("Do a calming sctivity to relax your body after the adventourous week")
elif day in ("Tuesday", "Thursday","Wednesday"):
   print("play with your friends")
else:
   print("Day not recognised:  check spellings")

if weather == "sunny" and homework == "yes":
   print("Head to the park great weather today")
if weather =="rainy" or homework == "yes":
   print("Pack your umbrella and finish your homework before you do anything else")

if not (homework == "yes"):
   print("Finish your homework")


