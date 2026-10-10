
valid = False

while valid==False:
    try:
        bill=float(input("Please enter your money here per person"))
        discountpercent=float(input("Please enter your discount percent"))
        numberofppl=int(input("What is the number of ppl"))
        finalbill=bill*numberofppl
        discountamount=discountpercent/100*finalbill
        print("this is the amount of discount",discountamount)
        print("this is the final bill",finalbill)
        
    except ValueError:
        print("Numbers only")

    except ZeroDivisionError:
        print("Number of people cant be zero")
    else:
        print(finalbill)
    finally:
        print("Attempt finished")
        break

