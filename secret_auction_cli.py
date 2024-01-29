#ask for bidders name, bid amount and, other bidders?
#can be one or more bidders
#keep track of bidder name and bid amount
bid_winner = ""
bidders = {}
other_bidders = True
def find_winner(bidders):
    winner = ""
    highest_bid = 0
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            winner = bidder
    return winner, highest_bid

while other_bidders == True:
    name = input("what is your name")
    bid_amount = int(input("what is your bid amount?"))
    is_other_bidders = input('is there other bidders? type: "yes" or "no"')
    bidders[name] = bid_amount
    if is_other_bidders == "no":
        other_bidders = False
        bid_winner = find_winner(bidders)
print(f'Congrats to {bid_winner} for winning the bid!')


