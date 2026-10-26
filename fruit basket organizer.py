basket1={"watermelon","orange",'banana','watermelon'}
basket2={"watermelon",'banana','apple'}

print(basket1)
print(basket2)

basket1.add("pear")
print(basket1)

commonfruits=basket1.intersection(basket2)
print(commonfruits)

import array as arr
fruitcount=arr.array("i",[1,2,3,4,5,4])
fruitcount.insert(3,5)
fruitcount.append(2)
print(fruitcount)


nooftimes=fruitcount.count(4)
print("This is how many times 4 has appeared",nooftimes)


fruitcount.reverse()
print("the reversed fruit count is",fruitcount)





"""

7) Count and reverse array values.
   a) Use `count()` to check how many times 4 appears.
   b) Use `reverse()` to reverse the order of the array.
   c) Print the count and reversed array.

8) Print the final summary.
   a) Print the class fruit basket organizer heading.
   b) Display both baskets, shared fruits, and fruit counts.
   c) Print a closing line to complete the summary.
"""