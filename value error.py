try:
    number=int(input("Please enter a number"))

    print("number:",number)

except ValueError as ex:
    print("Exception:",ex)