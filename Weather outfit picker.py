temp=int(input("Enter degrees celsius :"))

if temp < 12:
    outfit="Jacket"
    print("It is very cold")
    print("Please wear a", outfit)
else:
    outfit="T-shirt"
    print("Its hotter than usual")
    print("please wear a",outfit)

is_raining=input("Is it raining today (yes/no)")

if is_raining== "yes":
   print("Bring an umbrella")

wind_speed= int(input("what is the wind speed in your area?"))


if wind_speed > 30:
   print("Wear a windbreaker over your",outfit)

else:
    print("Dont wear your windbreaker over your outfit")

has_puddles=input("Are there puddles on the ground (yes/no)")

if has_puddles == "yes":
    shoes= "boots"
    print("Wear boots to ensure cleanliness")
else:
    shoes= "sneakers"
    print("The ground is dry so wear",shoes)


print("")
print("We have now finished the website")

# Use the print() function to display a blank line.
# Then display a message to let the user know that
# the weather check is complete.


# Use the print() function to display a weather
# outfit summary.
# Display:
# - The temperature entered by the user.
# - The outfit chosen.
# - Whether it is raining.
# - Whether a windbreaker is needed.
# - The shoes chosen.
# Add a heading and a closing line to make the summary
# easy to read.
