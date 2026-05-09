""" 
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes
"""
# import math module 
import math

# Get two numbers from the user.
manufactured_items = int(input("Enter the number of items: "))
item_per_box = int(input("Enter the number of items per box: "))

# Compute the number of boxes by dividing
# and then calling the math.ceil function.
num_boxes = math.ceil(manufactured_items / item_per_box)

# Display a blank line.
print()

# Display the results for the user to see.
print(f"For {manufactured_items} items, packing {item_per_box} items in each box, you will need {num_boxes} boxes")
