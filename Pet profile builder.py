print("===== WELCOME TO DOG ADOPTION CENTER ====")
print("You are free to check your options below")

class pet:
    pet="dog"
    def __init__(self,name,age):
        self.name=name
        self.age=age

Red=pet("Red",13)
max=pet("Max",20)
justice=pet("Justice",23)

print("Red is a {}".format(Red.pet))
print("Max is a {}".format(max.pet))
print("justice is a {}".format(justice.pet))

print("{} is {} years old".format(Red.name,Red.age))
print("{} is {} years old".format(max.name,max.age))
print("{} is {} years old".format(justice.name,justice.age))


print("They are all active but max is more active than the rest while red is the least active")
print("Just like his name justice is very kind but protective")
print("If you would like to adopt please move on to the next section")