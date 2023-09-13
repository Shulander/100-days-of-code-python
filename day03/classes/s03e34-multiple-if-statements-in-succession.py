print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You are tall enough to ride the roller coaster")
    age = int(input("What is your age? "))

    if age < 12:
        print("Child tickets are $5.00")
        total = 5
    elif age <= 18:
        print("Youth tickets are $7.00")
        total = 7
    else:
        print("Adult tickets are $12.00")
        total = 12

    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y":
        total += 3

    print(f"Your final bill is {total}")
else:
    print("Sorry, you are too short to ride the roller coaster")
