import random
def calculate_score():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_card=(random.sample(cards,2))
        computer_card=(random.sample(cards,2))
        user_score = sum(user_card)
        computer_score = sum(computer_card)
        return user_card,user_score,computer_card,computer_score

user_score ,user_card,computer_score,computer_card =calculate_score()
print( user_score ,user_card,computer_score,computer_card)

def game_core():
    ace=11
    user_choice=int(input("What is your Number?\n"))
    computer_choice= random.choice(computer_card)
    if len(user_card) == 2:
       if user_card == 11 and 10:
           print("user has blackjack")
    elif len(computer_card)==2:
        if computer_card == 11 and 10:
            print("computer has blackjack")


game_core()









