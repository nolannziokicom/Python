def total_calc(bill,tip_perc):
    total=bill*(1+0.01 * tip_perc)
    total=round(total,2)
    print(f"please pay{total}.")

total_calc(200,10)
# total = 200 * (1+0.01* 10)
"""
bodmas
200 *(1.01 * 10%)
200* 2.02
202sh
"""