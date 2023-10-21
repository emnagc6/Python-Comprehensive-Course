# greeting
print("Welcome to the Trip Cost Calculator!")

# Ask the user for number of days.
days_to_stay = float(input("How many days will you stay? "))

# Ask the user for hotel price.
price_per_night = float(input("How much does hotel cost per night? $"))

# Ask the user for flight price.
flight_price = float(input("How much does flight cost? $"))

# Ask the user for rental car price.
car_rent_price = float(input("If you need rental car please enter the price otherwise enter zero. $"))

# Ask for other expenses.
other_expenses = float(input("Enter other possible expenses: $"))

# Combine all expenses together and print with 2 digits after decimal places.
total_cost = (days_to_stay * price_per_night) + (flight_price) + (car_rent_price * days_to_stay) + (other_expenses)

# for 2 digits after decimal places
total_cost = round(total_cost, 2)

# print total cost
print(f"Total cost: ${total_cost}")