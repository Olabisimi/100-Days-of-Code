# TODO-1: Ask the user for input
name = input("Enter your name: ")
price = int(input("Enter your bid amount: "))
# TODO-2: Save data into dictionary {name: price}
bids={}
bids[name] = price
# TODO-3: Whether if new bids need to be added
any_more_bidders = input("Are there any other bidders? 'yes' or 'no':").lower()
    if any_more_bidders == "no":
        bidding_finished = True
    else:
        bidding_finished = False
# TODO-4: Compare bids in dictionary
highest_bid = 0
winner = ""
    for bidder in bids:
        bid_stated = bids[bidder]
        if bid_stated > bids[bidder]
        highest_bid = bid_amount
        winner = bidder









