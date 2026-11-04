class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blue",20)
alfred=parrot("alfred",13)
willow=parrot("willow",14)
woodie=parrot("woodie",34)

print("Blue is a {}".format(blu.species))
print("Alfred is a {}".format(alfred.species))
print("willow is a {}".format(willow.species))
print("woodie is a {}".format(woodie.species))


print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(alfred.name,alfred.age))
print("{} is {} years old".format(willow.name,willow.age))
print("{} is {} years old".format(woodie.name,woodie.age))


        