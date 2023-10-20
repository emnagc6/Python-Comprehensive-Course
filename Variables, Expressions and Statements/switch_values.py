a = 10
b = 5

#lets switch this values

#first way
a, b = b, a
print(a, b) #5, 10

#second way
a = a + b #a = 15, b = 5
b = a - b #a = 15, b = 10
a = a - b #a = 5, b = 10
print(a, b) #5, 10

#third way
temp = b
b = a
a = temp
print(a, b) #5, 10
