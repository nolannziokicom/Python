

print("=== Grocery Billing Queue ===\n")

low_price_items=0
medium_price_items=0
high_price_items=0
customers_served=0
total_sales=0
billing=True

while billing:
    name=input("Please enter your name")
    amountofitem=int(input("Please enter the amount of times your buying"))
    if amountofitem <= 0:
        print("You can't be giving items while your in the queue. Please enter a positive number")
        continue
    customer_total=0 
    item_number=1
    while item_number <= amountofitem:

        iname=input("Please enter the items name")
        price= int(input("Please enter the price of the item"))
        quantity=int(input("Please enter the quantity of the item"))
        if price <=0 or quantity <=0:
         
         print("Please input a positive number")
        else:
         item_total=price*quantity
        print(f"{iname}: {quantity}* {price} = {item_total}")
        customer_total+=item_total
        

        if price < 50:
          
        
          low_price_items +=quantity
        elif price <=100:
          medium_price_items += quantity
        else:
          high_price_items +=quantity
    item_number+=1

    customers_served +=1
    print(total_sales)
    print(f"\n Total bill for {name}: {customer_total}")
    print("Billing complete")

    again = input("Next customer(yes/no)")

    if again != "yes":
       
       billing=False
