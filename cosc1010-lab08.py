# Jose F. Negrete Oseguera
# UWYO COSC 1010
# Submission Date 11/05/2024
# Lab 08
# Lab Section:11
# Sources, people worked with, help given to: Help from TA's and from microsoft Co-pilot AI
# your
# comments
# here: for Part 1 I had more help from TA's during lab. for part 2 i used AI to help me solve issues and orginize my code. 
# for part 3 i was able to complet that with minimal AI help as i can understand math proces.  it gave me less truble, and using parts of part2





# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 




def check_for_int_or_float (string_to_check):
    """checks to see if the inputs are int or floats"""
    if (string_to_check.isdigit()):
        return int(string_to_check)
    if (string_to_check.count(".") == 1 and string_to_check.replace(".", "").isdigit()):
        return float(string_to_check)

    if (string_to_check[0] == "-" and string_to_check[1:].isdigit()):
        return int(string_to_check)
    if (string_to_check[0] == "-" and string_to_check[1:].replace(".", "").isdigit()):
        float
        return float(string_to_check)
    

print(check_for_int_or_float("-3"))

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def check_for_int_or_float(string_to_check):
    """checks to see if the inputs are int or floats"""
    if (string_to_check.isdigit()):
        return int(string_to_check)
    if (string_to_check.count(".") == 1 and string_to_check.replace(".", "").isdigit()):
        return float(string_to_check)

    if (string_to_check[0] == "-" and string_to_check[1:].isdigit()):
        return int(string_to_check)
    if (string_to_check[0] == "-" and string_to_check[1:].replace(".", "").isdigit()):
        float
        return float(string_to_check)

def Slope_int(m, b, a, an):
    """This is the y=mx+b formula"""
    return [(m*x)+b for x in range(a, an +1)]


while True:
    a_input = input("Enter a lower x bound. Must be a whole number, or 'exit' to exit: ")
    if a_input.lower() == "exit":
        break
    a = check_for_int_or_float(a_input)
    if not isinstance(a, int):
        print("Sorry, that is not a valid input for the lower x bound. It needs to be a whole number, try agin: .")
        continue

    an_input = input("Enter an upper x bound. Must be a whole number, or 'exit' to exit: ")
    if an_input.lower() == "exit":
        break
    an = check_for_int_or_float(an_input)
    if not isinstance(an, int):
        print("Sorry, that is not a valid input for the upper x bound. It needs to be a whole number, try again: ")
        continue

    if a > an:
        print("sorry the lowwer bound must be less than or equal too the upper bound, try agin: ")
        continue

    m_input = input("Enter an integer or decimal for the slope (m), or 'exit' to exit: ")
    if m_input.lower() == "exit":
        break
    m = check_for_int_or_float(m_input)
    if m is False:
        print("Sorry, that is not a valid input for the slope (m).")
        continue

    b_input = input("Enter an integer or decimal for the y-intercept (b), or 'exit' to exit: ")
    if b_input.lower() == "exit":
        break
    b = check_for_int_or_float(b_input)
    if b is False:
        print("Sorry, that is not a valid input for the y-intercept (b).")
        continue
        
    result = Slope_int(m, b, a, an)
    print(f"The result for your input variables is {result}")



print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
# ax^2 + bx + c = 0
# x = (-b +- square root b^2 - 4ac) / 2a

def check_for_int_or_float(string_to_check):
    """checks to see if the inputs are int or floats"""
    if (string_to_check.isdigit()):
        return int(string_to_check)
    if (string_to_check.count(".") == 1 and string_to_check.replace(".", "").isdigit()):
        return float(string_to_check)

    if (string_to_check[0] == "-" and string_to_check[1:].isdigit()):
        return int(string_to_check)
    if (string_to_check[0] == "-" and string_to_check[1:].replace(".", "").isdigit()):
        float
        return float(string_to_check)

def quafratic_form(a, b, c):
    under_sqrt = b**2 - (4*a*c)
    if under_sqrt < 0:
        return print("intiger under a square root can not equate less than 0")
    sqrt = (under_sqrt)**(1/2)
    x1 = (-b + sqrt)/ (2*a)
    x2 = (-b - sqrt)/ (2*a)
    return x1, x2


while True:
    quad_a = input("Enter a value for a: ")
    if quad_a.lower() == "exit":
        break
    a = check_for_int_or_float(quad_a)

    quad_b = input("Enter a value for b: ")
    if quad_b.lower() == "exit":
        break
    b = check_for_int_or_float(quad_b)

    quad_c = input("Enter a value for c: ")
    if quad_c.lower() == "exit":
        break
    c = check_for_int_or_float(quad_c)

    result = quafratic_form(a, b, c)
    print(f"The output is {result}")



