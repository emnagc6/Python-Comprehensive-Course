# Nested conditionals involve placing one or more conditional statements 
# (if, else if, else) inside another conditional statement. This structure allows 
# for more complex decision-making in programs. Essentially, nested conditionals 
# are used to test multiple conditions and execute different code blocks based on 
# those conditions.

# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

x = 10
y = 15
# Let's sort x and y

if x > y:
    print("x is greater than y")
else:
    if x < y:
        print("y is greater than x")
    else:
        print("x and y are equal")