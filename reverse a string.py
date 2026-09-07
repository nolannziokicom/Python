string=input("Please enter your string")
string2=("")
for letter in string:
    string2=letter+string2

print("Original string", string)
print("Reversed version", string2)