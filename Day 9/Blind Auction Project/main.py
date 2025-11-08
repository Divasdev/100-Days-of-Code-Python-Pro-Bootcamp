from art import  logo
print(logo)
bids={}

def biddingProcedure():
    user_input=input("What is your Name?\n")
    bid_price=int(input("what is your bid price?\n"))
    bids[user_input]=bid_price
bidding_finished=False

while not bidding_finished:
    biddingProcedure()
    other_bids=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bids == 'no':
        bidding_finished=True
highest_bid = 0
winner=""
for user_input in bids:
        bid_amount=bids[user_input]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner= user_input
print(f"The winner is {winner} with a bid of ${highest_bid}")







# TODO-4: Compare bids in dictionary

