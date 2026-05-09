"""
Write a program that will accept user input 
that describes a tire then calculate and display
the tire's volume.
Have the user enter a tire width in mm.
Have the user enter the aspect ratio.
Have the user enter the diameter of the wheel in inches.
Calculate and display the tire's volume.
Log the information in a text file.
current date (Do NOT include time)
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire (rounded to two decimal places)
"""
# EXCEEDING REQUIREMENT
# To exceed assignment expectation, i will be asking the 
# user if he/she wants to purchase tires withe the dimension she entered,
# If yes i will ask for quantity. 
# I will also add the quantity and phone number to the txt file

# Imports
from datetime import datetime
import math

# Ask the user for input 
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect of the tire in mm (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the tire's volume 
tire_volume = math.pi * width **2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000

# Display tire's volume
print(f"The approximate volume is {tire_volume:.2f} liters")

# Get current date from the computer's OS
current_date = datetime.now()

# Ask user if they are purchasing or not using loop
while True:
    purchase = input("Would you love to purchase this tire? (Yes/No): ").lower()

    if purchase in ["yes", "no"]:
        break
    else:
        print("Invalid response ⚠️  please enter yes or no")

phone_number = "N/A"
quantity = 0

if purchase == "yes":

    # Ask the customer for quantity
    quantity = int(input("How many tires would you like to purchase? "))
    phone_number = input("Please enter your phone number: ")

    # Compute response
    print(f"Thank You for ordering {quantity} {width}/{aspect_ratio}R{diameter} tire(s)! 🛞 ")
    print("Our sales team will contact you shortly for payment and delivery details")

else:
    print("Thank you! ☺️")
    print("Feel free to contact us anytime for tire service.") 

# Append to the end of the volumes.txt
with open("volumes.txt", "at") as volumes_file:
    print(
        f"{current_date:%Y-%m-%d}, "
        f"{width}, {aspect_ratio}, {diameter}, "
        f"{tire_volume:.2f}, {quantity}, {phone_number}",
        file=volumes_file
    )






