# Boolean expressions are constructs in programming that evaluate to either true or false. They are commonly used in control flow structures like if, while, and for loops to make decisions or to continue or break a loop. Boolean expressions are built using relational operators (like <, >, ==, !=, etc.), logical operators (like &&, ||, ! in languages 
x = (1==1)
print(x) # True
print(type(x)) # class -> bool

y = (1!=3)
print(y) # True
print(type(y)) # class -> bool

print(7>2) # True
print(2>7) # False
print(3>=3) # True

# is not operator
x = 3
y = 5
print(x is not y) # True
print(x is y) # False