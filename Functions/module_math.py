import math
import my_module

print(math.sqrt(25)) #5.0


#Constants
    # The math module in Python provides a number of mathematical constants that are ready 
    # for you to use in your programs without having to define them yourself. Some of the
    # most commonly used mathematical constants included in the math module are:

    # math.pi: The mathematical constant π, which is the ratio of the circumference of a circle to its diameter (approximately 3.14159).

    # math.e: The base of the natural logarithm (approximately 2.71828).

    # math.tau: The constant τ, which is the ratio of the circumference of a circle to its radius, and equal to 2 * math.pi (approximately 6.28318).

    # math.inf: A floating-point positive infinity; for negative infinity, you can use -math.inf.

    # math.nan: A floating-point “Not a Number” value, which is used to represent undefined or unrepresentable numerical results, such as the result of division by zero.

# Example usage of mathematical constants in the math module
circle_radius = 5
circle_circumference = 2 * math.pi * circle_radius
circle_area = math.pi * circle_radius ** 2

print("Circle circumference:", circle_circumference)
print("Circle area:", circle_area)

# Working with infinity
positive_infinity = math.inf
negative_infinity = -math.inf

# Using Not a Number (NaN)
not_a_number = math.nan

# Check if a value is NaN or infinity
print("Is positive_infinity an inf?", math.isinf(positive_infinity)) #True
print("Is not_a_number a NaN?", math.isnan(not_a_number)) #True

print(my_module.pi) #imported from my_module.py, 3.141592653589793