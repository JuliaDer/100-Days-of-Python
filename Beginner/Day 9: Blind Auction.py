from art import logo2
print(logo2)

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
        winner = max(bids, key=bids.get)
        bid_max = bids[winner]
        print(f"The winner is {winner} with a bid of ${bid_max}.")
    elif should_continue == "yes":
        continue
