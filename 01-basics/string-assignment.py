"""
Ask the user how many days until their birthday
and print an approx number of weeks until their birthday
weeks is = 7 days
decimals within the return is allowed
"""
days = int (input("How many days until your birthday : "))
weeks = days/7

print(f"Birthday in {round(weeks, 2)} weeks")