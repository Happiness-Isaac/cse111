# Example 1 contains a function named
#  print_cylinder_volume() with no parameters 
# that gets two numbers from the user: radius 
# and height and uses those numbers to compute 
# the volume of a right circular cylinder and 
# then prints the volume for the user to see.

import math 
 
 # Define a function named print_cylinder_volume.
def print_cylinder_volume():
    """Compute and print the volume of a cylinder.
    Parameters: none
    Return: nothing
    """
    # Get the radius and height from the user
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Compte the volume of the cylinder
    volume = math.pi * radius**2 * height
    
    # Print the volume of the cylinder
    print(f"Volume: {volume:.2f}")

print()
print()
print()

# Example 2 contains another version of the 
# print_cylinder_volume function. This second version
#  doesn’t get the radius and height from the user. 
# Instead, it gets input through its two parameters named radius and height.

import math
# Define a function named print_cylinder_volume.
def print_cylinder_volume(radius, height):
  """Compute and print the volume of a cylinder.
  Parameters
  radius: the radius of the cylinder
  height: the height of the cylinder
  Return: nothing
  """
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Print the volume of the cylinder.
  print(volume)

  # Because the second version of the print_cylinder_volume
  #  function accepts two parameters, it must be called with 
  # two arguments like this: print_cylinder_volume(2.5, 4.1)

  
print()
print()
print()

# Example 3 returns the volume instead of printing it, 
# which makes the function more reusable. Notice also 
# in example 3 that we changed the name of the function 
# from print_cylinder_volume to compute_cylinder_volume 
# because this version doesn’t print the volume but instead returns it.
import math
# Define a function named computer_cylinder_volume.
def compute_cylinder_volume(radius, height):
  """Compute and return the volume of a cylinder.
  Parameters
  radius: the radius of the cylinder
  height: the height of the cylinder
  Return: the volume of the cylinder
  """
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Return the volume of the cylinder so that the
  # volume can be used somewhere else in the program.
  return volume


print()
print()
print()

# Example 5 contains statements which are inside a user-defined function named main.
import math
# Define a function named main.
def main():
  # Get the radius and height from the user.
  radius = float(input("Enter the radius of a cylinder: "))
  height = float(input("Enter the height of a cylinder: "))
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Print the volume of the cylinder.
  print(f"Volume: {volume:.2f}")
# Start this program by
# calling the main function.
main()

print()
print()
print()

# Example 6 contains a complete program with two functions, 
# the first named main at line 4 and the second named 
# compute_cylinder_volume at line 14. At line 10, 
# the main function calls the compute_cylinder_volume function. 
# Notice that the compute_cylinder_volume function gets its input 
# through parameters and returns a result which makes this function 
# reusable in other programs, including programs that run automatically without a user.
import math
# Define the main function.
def main():
  # Get a radius and a height from the user.
  radius = float(input("Enter the radius of a cylinder: "))
  height = float(input("Enter the height of a cylinder: "))
  # Call the compute_cylinder_volume function and store
  # its return value in a variable to use later.
  volume = compute_cylinder_volume(radius, height)
  # Print the volume of the cylinder.
  print(f"Volume: {volume:.2f}")
# Define a function that accepts two parameters.
def compute_cylinder_volume(radius, height):
  """Compute and print the volume of a cylinder.
  Parameters
  radius: the radius of the cylinder
  height: the height of the cylinder
  Return: the volume of the cylinder
  """
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Return the volume of the cylinder so that the
  # volume can be used somewhere else in the program.
  # The returned result will be available wherever
  # this function was called.
  return volume
# Start this program by
# calling the main function.
main()