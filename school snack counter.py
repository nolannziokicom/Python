snack_box1={"bananas","apples","oranges","watermelon slices"}
snack_box_2={"sweets","cookies","sandwitches","apples","oranges"}
print("Snack box 1: ",snack_box1)
print("Snack box 2: ",snack_box_2)

snack_box1.add("sweets")
print("snack box one just got")

common_snacks=snack_box1.intersection(snack_box_2)
print("The common snacks are:",common_snacks)

import array as arr
snack_stock=arr.array("i"[2,3,4,5,7])
print("the snack stock is ",snack_stock)

snack_stock.append(2,3,4)
print("These are the added snacks")
print()
print("now u are allowed to pick your snacks")