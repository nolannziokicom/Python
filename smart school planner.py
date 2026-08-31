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



# c) If the condition is True, print

# "Homework    : Not done yet. Finish it before going out!".

# 8) Combine the AND, OR, and NOT operators:

# a) Use an `if` statement to check whether `weather` is "rainy"

# AND `homework` is NOT "yes".

# b) If True, print

# "Best plan   : Stay in, finish homework, then watch your favourite show.".

# c) Use `elif` to check whether `weather` is "sunny",

# `homework` is "yes", AND `day` is NOT "Saturday" or "Sunday".

# d) If True, print

# "Best plan   : All set for a great school day - you are prepared!".

# e) Use another `elif` to check whether `day` is "Saturday" or "Sunday"

# AND `weather` is "sunny".

# f) If True, print

# "Best plan   : Perfect weekend weather - head outside and have fun!".

# g) Use `else` if none of the previous conditions are True.

# h) Print "Best plan   : Take it one step at a time - you have got this!".

# 9) Display the final message:

# a) Use `print()` to create a blank line.

# b) Use `print()` to display "Plan complete! Have a wonderful day!".
