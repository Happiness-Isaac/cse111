def college (name):
    print(f"Hello {name}! welcome to school.")
user = input("What is your name? ")
college (user)

print()
print()
print()


def add(first, second):
    """
    Adds two numbers together and return the result
    """

    result = first + second
    return result

x = 3
y = 6
total = add(x, y )
print(total)

total = add(y, y)
print(total)

print()
print()
print()

def get_positive_value(prompt_text):

    """"
    prompt the user for a value, and re-prompt 
    them if the original value is negative
    """

    # prompt for the value 
    value = float(input(prompt_text))

    # check if the value is positive and re-prompt if needed
    while value < 0:
        print("Sorry, the value cannot be negative.")

        value = float(input(prompt_text))

    # return value
    return value


length = get_positive_value("What is the length of the rectangle? ")
width = get_positive_value("What is the width of the rectangle? ")

area = length * width

print(f"The area is {area}")