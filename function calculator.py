calculate=True
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide (a,b):
    return a/b
while calculate:
    print("You have 5 choices to choose from in this application")
    print("1.Add")
    print("2.subtract")
    print("3.Multiply")
    print("4.divide")
    print("5.exit")
    choice=int(input("Choose a choice from 1-5:"))
    num1=float(input("Enter a number for calculation:"))
    num2=float(input("Enter the second number for calculation:"))
    if choice ==1:
       addition=num1+num2
       print("Your answer is",addition)
    elif choice ==2:
        subtraction=num1-num2
        print("Your answer is",subtraction)
    elif choice==3:
        multiplication=num1*num2
        print("Your answer is",multiplication)
    elif choice==4:
        divition=num1/num2
        if num2==0:
            print("Zero division error")
        print("Your answer is",divition)
    elif ValueError:
        print("this means a value error has been detected.Please follow the instructions given")
    else:
        print("Please input real numbers")
        
    
    

    

    

