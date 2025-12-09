MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }

}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Handle the first user input
machine_on=True
while machine_on:
  user_choice=input("What would you like? (espresso/latte/cappuccino):")
  if user_choice=="off":
      machine_on=False
      #Implement the "report" command
  elif user_choice=="report":
       print("Water:",resources["water"],"\nMilk:",resources["milk"],"\nCoffee:",resources["coffee"])
  #: Check if resources are sufficient for the selected drink

  else:
      if user_choice=="espresso":
            print(MENU["espresso"]["ingredients"])

      if user_choice=="latte":
                print(MENU["latte"]["ingredients"])

      if user_choice=="cappuccino":
                print(MENU["cappuccino"]["ingredients"])
      else:
         print("Enough Resources")
  print("Please Insert Coins")
  quarter_coin=int(input("Enter Your Quarter Coins:\n"))
  dimes_coin = int(input("Enter Your Dimes Coins:\n"))
  nickels_coin = int(input("Enter Your Nickel Coins:\n"))
  pennies_coin = int(input("Enter Your Pennies Coins:\n"))

  user_total= (quarter_coin*0.25) + (dimes_coin*0.10) + (nickels_coin*0.05) +(pennies_coin*0.01)
  user_total_coins=round(user_total,3)
  print(f"You inserted:$",user_total_coins)










