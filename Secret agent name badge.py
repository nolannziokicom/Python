#1) Ask for agent details.
print("Enter your details")
name=input("Enter your name:")
gadget=input("What is your favorite gadget:")
print("Welcome to Secret agent headquarters ", name, "here is your weapon just as you like it",gadget)

Agent_number=4
Speed=10.3
mission_count=3
active_status=True
height=140

print("Here r your details-str no1.is your agent number no2 is your number of missions no3 is your active status no4 is your speed like your vehicles speed and no5 is your measured height in centimeteres", Agent_number,mission_count,active_status,Speed,height)


print(type(Agent_number))
print(type(Speed))
print(type(mission_count))
print(type(active_status))
print(type(height))


""""
3) Display each value and its data type.
   a) Print the agent name and gadget.
   b) Print number, rating, mission count, height, and active status.
   c) Use `type()` to show the data type of each value.

4) Convert values into text.
   a) Use `str()` to convert numbers into strings.
   b) Convert the Boolean value into text.
   c) Print the converted values and their new data types.

5) Create a secret code name.
   a) Use slicing to get the first three letters of the name.
   b) Use negative indexing to get the last letter.
   c) Join both parts to create the code name.

6) Reverse the gadget name.
   a) Use slicing with `[::-1]` to reverse the gadget text.
   b) Print the reversed gadget name.

7) Build the badge message.
   a) Create separate lines for the agent badge.
   b) Use string concatenation to join text and variables.
   c) Use `.upper()` to make important badge text uppercase.

8) Print the secret agent badge.
   a) Print a badge heading.
   b) Print all badge lines one by one.
   c) Print a closing line to complete the badge.
"""