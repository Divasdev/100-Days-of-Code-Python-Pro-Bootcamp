from idlelib.configdialog import changes

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

money=0.0


# Handle the first user input
machine_on=True
while machine_on:
  user_choice=input("What would you like? (espresso/latte/cappuccino):").lower()
  if user_choice=="off":
      machine_on=False
      #Implement the "report" command



  elif user_choice=="report":
       print("Water:",resources["water"],"\nMilk:",resources["milk"],"\nCoffee:",resources["coffee"])

       print("Money:$",money)
  # Check if resources are sufficient for the selected drink

  else:
    if user_choice in MENU:
      # show ingredients for the chosen drink
      print(MENU[user_choice]["ingredients"])

      # Check resources for the chosen drink
      ingredients = MENU[user_choice]["ingredients"]
      for item, required in ingredients.items():
        if resources.get(item, 0) < required:
          print(f"Sorry there is not enough {item}.")
          break
      else:
        # All resources sufficient — process coins
        print("Please Insert Coins")
        quarter_coin = int(input("Enter Your Quarter Coins:\n"))
        dimes_coin = int(input("Enter Your Dimes Coins:\n"))
        nickels_coin = int(input("Enter Your Nickel Coins:\n"))
        pennies_coin = int(input("Enter Your Pennies Coins:\n"))

        user_total = (quarter_coin * 0.25) + (dimes_coin * 0.10) + (nickels_coin * 0.05) + (pennies_coin * 0.01)
        user_total_coins = round(user_total, 2)
        print(f"You inserted: ${user_total_coins:.2f}")

        cost = MENU[user_choice]["cost"]
        if user_total_coins < cost:
          print("Sorry that's not enough money. Money refunded.")
        else:
          change = round(user_total_coins - cost, 2)
          money += cost
          if change > 0:
            print(f"Here is ${change:.2f} dollars in change.")
          print("Transaction Successful.")
          print(f"Money: ${money:.2f}")

          # Deduct the ingredients
          for item, amount in MENU[user_choice]["ingredients"].items():
            resources[item] -= amount

          print(f"Here is your {user_choice}. Enjoy!")
    else:
      print("Invalid selection.")
