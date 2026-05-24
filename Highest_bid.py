import os

def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
        bid_price=bidder_details[bidder]
        if bid_price>highest_bid:
            highest_bid=bid_price
            winner=bidder
    print(f"The winner in the auction is {winner} with the amount of {highest_bid}")
bidder_data={}
end_of_bid = False
while not end_of_bid:
    name=input("Enter the name: ")
    price=int(input("Price: "))
    bidder_data[name]=price    #name = key and price = value
    any_biders=input("Are there any bidders 'yes' or 'no': ")
    if any_biders == 'no':
        end_of_bid=True
        find_winner(bidder_data)
    elif any_biders == 'yes':
        os.system('cls')