def calculate_change(paid,price):
    changes=paid-price
    return changes

snack_price=25
print("Snack vending machine")
print(f"This snack costs {snack_price}units")
print("Accepted coins: 1,5,10,20\n")

total_inserted=0
coins_inserted=0

while True:
    coin=int(input( "Insert coins(1,5,20,25)"))

    if coin != 1 and coin!=5 and coin!=20 and coin!=25:
        print("Invalid coin")
        continue

    total_inserted += coin
    coins_inserted+= 1
    print(f"inserted {coin}. Total so far.{total_inserted}\n")

    if total_inserted >= snack_price:
        print("Enough money inserted\n")
        break
change_due= calculate_change(total_inserted,snack_price)

print("Dispencing your snack")


if change_due==0:
    pass
else:
    print(f"Here is your change{change_due}units")