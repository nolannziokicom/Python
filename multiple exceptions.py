try:
    num1,num2=eval(input("Please input 2 number1 with number one being bigger than number 2 "))
    result=num1/num2
    print(result)

except ZeroDivisionError:
    print("Zero division error!!!")
except SyntaxError:
    print("Put a coma in between the numbers eg 1,2 and check the problems section")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will run no matter the circumstance")

