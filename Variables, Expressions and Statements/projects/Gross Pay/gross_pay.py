hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))

gross_pay = round(hours * rate, 2) # write 2 digits after the decimal
print(gross_pay)