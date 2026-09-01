print("Smart day school planner")
print("Answer these three questions and i'll plan your day \n")



day = input("What day is it?").strip().capitalize()
weather= input("What is the weather today: (Sunny/rainy/cloudy)").strip().lower()
homework =input("Have you finished your homework?").strip().lower()

print("")

print("-"* 35)

if day in ("Saturday","Sunday"):
   print("Enjoy your weekend")
elif day == "Monday":
   print("First school day stay focused")
elif day =="Friday":
   print("Last day of school ensure you have packed everything")
elif day in ("Tuesday", "Thursday","Wednesday"):
   print("Stay focused half way through the week")
else:
   print("Day not recognised:  check spellings")

if weather == "sunny" and homework == "yes":
   print("Head to the park great weather today")
if weather =="rainy" or homework == "yes":
   print("Pack your umbrella and finish your homework before you do anything else")

if not (homework == "yes"):
   print("Finish your homework")


