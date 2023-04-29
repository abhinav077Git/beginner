# from art_secret import logo
# print(logo)
# bid_price_dictionary={}
# other_bid=True

# def bid_winner(bidding_record):
#     highest_bid=0
#     winner=""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"winner is {winner} with bid amount {highest_bid}")

# while other_bid:
#         name=input("Enter your name: ")
#         bid_price=int(input("Enter your bid price: "))
#         # bid_price_dictionary[name]=name
#         bid_price_dictionary[name]=bid_price
#         # bid_price_dictionary["other_user_bid"]=[other_to_bid]
#         print(bid_price_dictionary)
#         other_user_bid=input("Other user want to bid...Enter Yes or No: ")
#         if other_user_bid.casefold() == "no":
#             other_bid = False
#             bid_winner(bid_price_dictionary)
#         else:
#             other_bid=True
# # print(bid_price_dictionary)

####################################################
def bid_winner(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"winner is {winner} with bid amount {highest_bid}")

bid_price_dictionary={
    "Abhinav" : 123,
    "Ankit" : 246
}

bid_winner(bid_price_dictionary)
###################################################

    
