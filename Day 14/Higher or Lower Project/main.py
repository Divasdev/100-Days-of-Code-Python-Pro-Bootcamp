from pyexpat.errors import messages

from game_data import data
import random

print("Welcome to Higher-Lower Instagram game")




person_A=random.choice(data)
person_B=random.choice(data)
print(f"COMPARE A-:{person_A['name']},{person_A['description']},from {person_A['country']}.")
print('v/s')
print(f"COMPARE B-:{person_B['name']},{person_B['description']},from {person_B['country']}.")

user_input=input("who has more instagram followers? Type 'A' or 'B':")


currentScore =0
def game_core(person_A,person_B,user_input):

    global currentScore
    a_follower=person_A[ 'follower_count']
    b_follower=person_B[ 'follower_count']

    is_correct=(
    (user_input == 'A' and a_follower > b_follower) or
    (user_input =='B' and b_follower>a_follower)
    )
    if is_correct:
        currentScore+=1
        return True, f"You are right!.Current Score : {currentScore}"
    else :
        return False, f"Sorry that's wrong!.Final score:{currentScore}"

def get_random_account(exclude=None):
    account=random.choice(data)
    while exclude is not None and account ==exclude:
        account=random.choice(data)
    return account



game_on=True
person_A=get_random_account()
while True:

    person_B = get_random_account(exclude=person_A)

    print(f"COMPARE A-:{person_A['name']},{person_A['description']},from {person_A['country']}.")
    print('v/s')
    print(f"COMPARE B-:{person_B['name']},{person_B['description']},from {person_B['country']}.")


    user_input = input("who has more instagram followers? Type 'A' or 'B':")

    is_correct,messages=game_core(person_A,person_B,user_input)
    print(messages)
    if not is_correct:
        game_on=False
    else:
        person_B=person_A
    print(game_core())

