grade_book={"name,1":"Alex",
            "score,1": "40/50",

            "name,2": "Alfred",
            "score,2":"50/50",

            "name,3":"Alice",
            "score,3":"45/50",

            "name,4":"Caleb",
            "score,4": "39/50",

            "name,5":"Ava",
            "score,5":"45/50"
            }
print(grade_book)
names=["Alex","Alfred","Alice","Caleb","Ava"]
scores=[40,50,45,39,45]

for i in scores:
    i += 1
    add=i+i
    
    average=add/len(names)
    print(average)

top_scorer=max(
    scores
)
print(top_scorer)
bottom_scorer=min(scores)
print(bottom_scorer)

index1=names.get(0)
index2=names.get(1)
index3=names.get(2)
index4=names.get(3)
index5=names.get(4)
print("Choose according to the index: name 1 is index 1 etc")

names=input("Please enter the name of the learner your looking for?")
index=int(input("please enter your index"))

if names == "Alex" and index == 1:
    print("You have chose alex. He will come shortly")
    print("His score is",40)
elif names == "Alfred" and index ==2:
    print("You have chose alfred he will come shortly")
    print("His score is",50)
elif names== "Alice" and index ==3:
    print("Alice is coming shortly")
    print("Her score is",45)
elif names== "Caleb" and index==4:
    print("Caleb is coming shortly")
    print("his score is",39)
elif names=="Ava" and index==5:
    print("Ava is coming shortly")
    print("Her score is",45)
else:
    print("sry your students name is not here. Go check in the office")


