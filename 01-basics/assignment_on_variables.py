"""
You have $50
You buy an item that is $15
With a tax of 3%
Print how much money you have left
"""

myCash = 50
item_price = 15
tax_percent = 0.03
cost = item_price + (item_price * tax_percent)

print(f"My remaining balance : {myCash - cost}")
