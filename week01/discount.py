# Imports
from datetime import datetime

# Constants 
# (They never change throughout the program.
#  and they are always in capital letter)
SALES_TAX_RATE = 0.06 
DISCOUNT_RATE = 0.10

discount = 0
subtotal = 0

# Ask th user for a price and quantity
price = 1
while price != 0:
    # Ask the user for a price
    price = float(input("Enter a price: "))
    if price != 0:
        # Ask the user for a quantity
        quantity = int(input("Enter a quantity:"))

        subtotal += (price * quantity)
print(f"The subtotal is ${subtotal:.2f}")

# Figures out the day and week
current_date_time = datetime.now()
current_day_of_week = current_date_time.weekday()

#calculate the discount
if current_day_of_week == 1 or current_day_of_week == 2:
    if subtotal < 50:
        print(f"You only need to spend ${(50 - subtotal):.2f} more to qualify for a discount! ")
    else:
        discount = subtotal * DISCOUNT_RATE
        print(f"You've earned a discount of ${discount:.2f}")

# Calculate the sales tax 
sales_tax = (subtotal - discount) * SALES_TAX_RATE
print(f"The sales tax is ${sales_tax:.2f}")

# Calculate the total amount
total = (subtotal- discount) + sales_tax
print(f"The total is ${total:.2f}")