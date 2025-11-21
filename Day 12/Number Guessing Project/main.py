import random

print("Welcome  to Number Guessing Game!!")
print("I'm thinking of a number between 1 and 100.")

difficulty_level=input("Choose a difficulty.Type 'easy' or 'hard' :")
number = list(range(1, 101))
random_number_1to100 = random.choice(number)
user_guess = int(input("Make a guess:  "))


def game_attempts():
    global attempts
    if difficulty_level == 'easy':
        print("You Have 10 attempts remaining to guess the number.")
        attempts = 10
    elif difficulty_level == 'hard':
        print("You have 5 attempts remaining to guess the number.")
        attempts = 5

game_attempts()

def userGuess():
    if user_guess<random_number_1to100:
        print('Too low.')
    elif user_guess>random_number_1to100:
        print("Too high.")
    else:
            print("Correct")

while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess < random_number_1to100:
        print("Too low.")
    elif guess > random_number_1to100:
        print("Too high.")
    else:
        print("Correct!")
        break

    attempts -= 1
    print(f"You have {attempts} attempts remaining.")

if attempts == 0:
    print("You ran out of attempts. You lose!")
