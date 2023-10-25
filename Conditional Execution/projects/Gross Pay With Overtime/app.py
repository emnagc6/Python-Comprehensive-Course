hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))

if hours > 40:
    overtime = hours - 40
    gross_pay = 40 * rate + (overtime * 1.5 * rate)
else:
    gross_pay = hours * rate


gross_pay = round(gross_pay, 2) # write 2 digits after the decimal
print(gross_pay)