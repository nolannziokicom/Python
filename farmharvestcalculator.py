
field1=143
field2=154
field3=47
field4=77
field5=3411

total=field1 + field2 + field3 + field4 + field5
average= total / 5
price_per_kg=27
total_earnings= price_per_kg * total

print("total harvest: ", total)
print("Average:", average)
print("money earned:", total_earnings)


bags= total // 25
leftovers= total% 25

print( "Bags filled :",bags)
print("Left overs from couldn't fit:",leftovers)


last_year=4500;
print("Better than last year;", total > last_year)
print("Same as last year;", total == last_year)
print("At least as good;", total >= last_year)



total += 1000
print( "Added crop from friends with total:",total )

total -=332
print("Saved crop for next year:",total)

bags= total//25
print("Total bags:", bags)


"""""



7) Use assignment operators.
   a) Use `+=` to add bonus crop to the total.
   b) Use `-=` to subtract grain saved as seeds.
   c) Print the updated harvest after each change.

8) Calculate the final bag count.
   a) Use floor division again after adjustments.
   b) Print the final number of bags packed.
"""


