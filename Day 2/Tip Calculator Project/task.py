print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_bill = bill + (bill * tip_as_percent)
final_amount = total_bill / people

# Round to 2 decimal places (like currency)
final_amount = round(final_amount, 2)

print(f"Each person should pay: ${final_amount}")


