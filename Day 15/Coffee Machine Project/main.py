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

  elif user_choice=="espresso":
        print(MENU["espresso"]["ingredients"])
  elif user_choice=="latte":
            print(MENU["latte"]["ingredients"])
  elif user_choice=="cappuccino":
            print(MENU["cappuccino"]["ingredients"])



  else:
      print(user_choice)














