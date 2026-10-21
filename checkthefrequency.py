test_dict={
    "water":23,
    "is":23,
    "not":24,
    "wet":64
}

print("The original dictionary is" + str(test_dict))

j=23
res=0

for key in test_dict:
    if test_dict[key] == j:
        res=res+1

print("The frequency of j is", str(res))