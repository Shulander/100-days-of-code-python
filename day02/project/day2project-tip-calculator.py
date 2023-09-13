# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill?7
# Each person should pay: $19.93

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100 + 1
people = int(input("How many people to split the bill? "))

per_person = round(bill * tip / people, 2)
# add trailing zeroes 33.6 -> 33.60
per_person_with_zeroes = "{:.2f}".format(per_person)
print(f"Each person should pay: ${per_person_with_zeroes}")
