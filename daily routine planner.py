print("Answer these questions for me to make your schedule for today")
print()

weather=input("Please tell us the weather in your area?")
homework=input("Have you finished your homework?")
day=input("What day is it (Write starting with a capital letter)")

if day in ("Saturday","Sunday" ):
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


