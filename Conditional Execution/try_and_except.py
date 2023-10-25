#In Python, the try and catch mechanism is used for exception handling.


try:
    salary = int(input("what is your salary: $"))
except:
    print("there was an error")
else:
    if salary > 2000:
        print("you are eliable for the mortgage!")
    else:
        print("you're not eligable for the mortgage!")
finally:
    print("thanks for using our calculator!")