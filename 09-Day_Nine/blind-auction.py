import os
bidding_end = False
bid = {}

def highest_bidder(bidding_file):
    score = []
    for key, value in bid.items():
        score.append(value)

    search_value = max(score)
    
    for key, value in bid.items():
        if value == search_value:
            print(f'{key} won')

while not bidding_end:
    name = input('Please enter your name: ')
    money = int(input('Please enter your bid: '))

    bid[name] = money

    option = input('is there anyother bidder? type "yes" or "no"\n:').lower()

    if option == 'yes':
        os.system('clear')
    elif option == 'no':
        bidding_end = True
        highest_bidder(bid)
