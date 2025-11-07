"""#print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("what is your age"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age >=18:
        print("Your ticket price is $12")
    elif age>12 & age<18:
        print("Your ticket price is $7")
    else:
        print("Your ticket price is $5")

else:
    print("Sorry you have to grow taller before you can ride.")"""

weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi<18.5:
    print("You are underweight")
elif bmi >=18.5 and bmi<25:
    print("You are normal weight")
else:
    print("You are overweight")

