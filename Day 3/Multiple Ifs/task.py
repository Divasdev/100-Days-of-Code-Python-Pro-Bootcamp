print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket $5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickets $7.")
    else:
        bill =12
        print("Adult tickets $12.")
    take_Photos = input("Do you want to take photos???(type Y for Yes and n for No.")
    if take_Photos == 'Y':
        bill +=3
    print(f"Your final bill is {bill}")


else:
    print("Sorry you have to grow taller before you can ride.")
