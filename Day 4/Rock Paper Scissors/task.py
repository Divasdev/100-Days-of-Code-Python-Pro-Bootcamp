import  random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice =int(input("What do you choose? Type 0 for Rock, for Paper or 2 for scissors:\n "))
print("you choose:")
if user_choice  == 0:
    print(rock)
elif user_choice ==1:
    print(paper)
elif user_choice==2:
    print(scissors)
else:
    print("invalid move")




computer_move= random.randint(0,2)
print(" Computer chose:")
if computer_move  == 0:
    print(rock)
elif computer_move ==1:
    print(paper)
elif computer_move==2:
    print(scissors)

if user_choice == computer_move:
    print("Its a draw")
elif (user_choice == 0 and computer_move == 2) or \
         (user_choice == 1 and computer_move == 0) or \
         (user_choice == 2 and computer_move == 1):
    print("You win! 🎉")

else:
    print("You losse!")


