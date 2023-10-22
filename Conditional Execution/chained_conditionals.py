# In Python, chained conditionals use the elif keyword (short for "else if") to check multiple conditions in a sequential manner. Unlike nested conditionals where one conditional statement is embedded within another, chained conditionals are a flat sequence of conditions to be checked. Once a condition is met, the corresponding code block is executed, and the rest of the conditions are skipped.

# if condition1:
#     do this
# elif condition2:
#     do this
# else:
#     do this

x = 15

if x < 10:
    print("x is less than 10")
elif x < 20:
    print("x is between 10 and 19")
elif x < 30:
    print("x is between 20 and 29")
else:
    print("x is 30 or greater")
