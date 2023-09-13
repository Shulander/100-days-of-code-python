print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You are tall enough to ride the roller coaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.00 for the ticket")
    elif age <= 18:
        print("Please pay $7.00 for the ticket")
    else:
        print("Please pay $12.00 for the ticket")
else:
    print("Sorry, you are too short to ride the roller coaster")
