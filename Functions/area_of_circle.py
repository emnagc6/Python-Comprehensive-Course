import math

radius = int(input("Enter Radius: "))
pi = math.pi

area = (pi * math.pow(radius,2))
area = round(area, 2)
print(f"The area of circle is {area}")