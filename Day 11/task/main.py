import random
def calculate_score():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_card=(random.sample(cards,2))
        computer_card=(random.sample(cards,2))
        user_score = sum(user_card)
        computer_score = sum(computer_card)
        return user_card,user_score,computer_card,computer_score

user_card,user_score,computer_card,computer_score =calculate_score()
print( user_card,user_score,computer_card,computer_score)

def user_has_blackjack():
    if len(user_card)==2:
        if 10 in user_card and 11 in user_card:
          return  "you win "


def computer_has_blackjack():
    if len(computer_card)==2:
        if 10 in computer_card and 11 in computer_card:
         print("Computer has blackjack. You lose.")

result_user=user_has_blackjack()
result_computer=computer_has_blackjack()


def blackjack_result():
    '''if result_user and result_computer:
        print("Both have blackjack — Draw")'''
    if result_user:
        print(result_user)
    elif result_computer:
        print(result_computer)
    else:
      print("play again ")

def game_core():
    if user_score > 21:
        if 11 in user_card:
            if user_score > 21:
                print("USER LOSE ")
    else:
      user_next_move=input("Do you want to get another card? Type 'y' for YES and 'n' for NO")
      if user_next_move=="y":
          calculate_score()
      else:
          if computer_score<17:
              calculate_score()
          elif computer_score>21:
              print("USER YOU WIN")
          else:
              if computer_score<user_score:
                  print("USER WIN.COMPUTER LOSE ")
              elif computer_score>user_score:
                  print("USER LOSE. COMPUTER WINS")
              else:
                  print("THE GAME'S DRAW")



blackjack_result()
game_core()







