# Corrected version of the sum function example

# Original broken code:
# def sum (x):
#     return  x= 10
# print(sum)

# Problems found:
# 1. `return x = 10` is a syntax error - you cannot assign inside a return.
# 2. `print(sum)` prints the function object, not a result - you need parentheses.
# 3. Using the name `sum` shadows Python's built-in sum() function.

# Fixed version - option 1: returns x plus a value
def my_sum(x):
    return x + 10

# Fixed version - option 2: returns a fixed value
def my_fixed_sum(x):
    return 10

# Calling the functions with parentheses
print(my_sum(5))        # Output: 15
print(my_fixed_sum(5))  # Output: 10

