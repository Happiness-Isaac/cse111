"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
Write a Python program named heart_rate.py that asks for a person’s age
and computes and outputs the slowest and fastest rates necessary to strengthen his heart
""" 
age = int(input("What is your age? "))

#computes and outputs the slowest and fastest rates necessary to strengthen his heart

max_rate = 220 - age
slowest = max_rate * 0.65
fastest = max_rate * 0.85 
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.")

