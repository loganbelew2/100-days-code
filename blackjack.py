from random import choice
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
play_blackjack = input("do you want to play blackjack?: 'y' or 'n'\n")
while play_blackjack == "y":
    user_cards = [choice(cards), choice(cards)]
    print(type(user_cards))
    computer_cards = [choice(cards), choice(cards)]
    users_total = sum(user_cards)
    computers_total = computer_cards[0] + computer_cards[1]
    print(f'your cards are {user_cards[0]} and {user_cards[1]}, current score: {user_cards[0] + user_cards[1]}')
    print(f'computers first card is {computer_cards[0]}')
    another_card = input('type "y" to get another card or "n" to pass: ')
    if another_card == 'y':
        user_cards.append(choice(cards))
    if users_total > 21 and 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
    print(f'your final hand: {user_cards}, final score: {users_total}')
    print(f'computers final hand: {computers_total}')
    if users_total > 21:
        print('you lose you went over 21')
    else:
        print('you win') if users_total >= computers_total else print('you lose')
    play_blackjack = input('do you want to play again: "y" or "n"\n')