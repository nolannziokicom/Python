items=["sharpener","pencil","crayons","ruler"]
stock_counts=[10,20,50,30]

inventory={item:count for item,count in zip(items,stock_counts)}

print(inventory)

in_stock_items=[item for item in items if inventory[item] > 0 ]
print(in_stock_items)

chosen_stationary=input("Please enter the stationary you want to buy?")
if chosen_stationary not in inventory or inventory[chosen_stationary] ==0:
    print(chosen_stationary,"is out of stock. Please come again later")
    exit()

prices=[10,20,60,30]
markup=int(input("Please enter the markup price of the following stationary"))

marked_up_prices=list(map(lambda p:p+ markup,prices))
print("marked up prices: ", marked_up_prices)

item_index=items.index(chosen_stationary)
chosen_price=marked_up_prices[item_index]
print("Price of",chosen_stationary, "after markup",chosen_price)

inventory[chosen_stationary]=inventory[chosen_stationary]-1
print(chosen_stationary,"bought. Remaining stock:",inventory[chosen_stationary])

