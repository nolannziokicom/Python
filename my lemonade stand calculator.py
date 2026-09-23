def greetcustomer():
    print("Welcome to the lemonade stand")
    print("Fresh lemonade, made just for you")

greetcustomer()

price_per_cup=float(input("Enter the price of each cup"))
cups_sold=int(input("enter the amount of cups sold"))

def calculate_total(price,cups):
    total=price*cups
    return total

total_cost= calculate_total(price_per_cup,cups_sold)
print(total_cost)

rounded_total=round(total_cost,2)
print("Total cost",rounded_total)

amount_paid=float(input("Enter the amount paid:"))

def calculate_change(paid,total):
    change=paid-total
    return change

change_due= calculate_change(amount_paid,rounded_total)
rounded_change=round(change_due,2)
print("Change:",rounded_change)


def thank_you_message(cups):
    

    if cups >=5:
        print("Wow! Big order thank you for supporting us")
    else:
        print("Thank you for stopping by the stand")

thank_you_message(4)


