import random
import os
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return 'loss, computer has a blckjack!'
    elif user_score == 0:
        return 'Win! you have a blackjack!'
    elif user_score > 21:
        return 'you went over! you lose'
    elif computer_score > 21:
        return 'computer went over! you win'
    elif user_score > computer_score:
        return 'you win'
    else:
        return 'you lose'
def play_game():
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'    your cards {user_cards} and current score: {calculate_score(user_cards)}')
        print(f'    computer\'s first card: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0  or user_score > 21:
            is_game_over = True
        else:
            deal_new_card = input('type "y" to deal new card or type "n" to pass\n:')
            if deal_new_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'\nyour final deck is {user_cards} and your final score is: {user_score} ')
    print(f'computer final deck is {computer_cards} and computers final score is: {computer_score} ')
    print(compare(user_score, computer_score))

while input('\n*_* do you want to play a game of blackjack? Y/N: ').lower() == 'y':
    os.system('clear')
    play_game()