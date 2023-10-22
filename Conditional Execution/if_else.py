# if condition:
#     do this
# else:
#     do this

# Let's make a mortgage calculator
print("Welcome to mortgage calculator!")
salary = int(input("Enter your salary: $"))

# indentations are important!
if salary >= 2000:
    print("You are eligable for mortgage!")
    credit_score = int(input("Enter your credit score: "))
    if credit_score >= 800:
        print("Your interest rate is %4")
    else:
        print("Your interest rate is %6")
else:
    print("You are not eligable for mortgage!")

# pass keyword
if salary >= 1_000_000:
    print("You are rich")
else:
    pass # if we want to add our code here later, we can use pass keyword.