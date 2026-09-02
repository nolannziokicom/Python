print("Welcome to custom ride builder")


print("Choose option 1 or option 2")
print("Option one= bike")
print("Option two=car")
option_chooser=input("Choose here: input your answer(1/2)")


if option_chooser=="1":
    print("You have chose option 1= bike")
    print("Option a is a kenchii mountain bike and\n option b is a honda motorbike")

    bike_input=input("Choose option a or b as a bike")
    if bike_input=="a":
        print("You have chose kenchii mountain bike")
        print("Kenchii mountain bike=100km/h")
        print("This is fit for mountains")
    else:
        print("You have chosen honda motorbike")
        print("Honda motorbike = 200km/h")
        print("This motorbike is specially built for cities")
elif option_chooser=="2":
    print("You have chosen cars")
    print("Option 1 is a tesla supercar and\n option 2 is a jeep")
    car_input=input("Choose option 1 or 2")
    if car_input== "1":
        print("You have chosen tesla supercar")
        print("This car can go upto 500km/h")
        print("it's electric")
        print("Its best for cities")
    else:
        print("You have chosen jeep")
        print("It is best for offroad trips")
        print("300km/h")















