import random

# data
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
player_hand = []
dealer_hand = []
sum_player = 0
sum_dealer = 0
game_over = False
passed = False


def display_card():
    show_player = player_hand.copy()
    show_dealer = dealer_hand.copy()

    for i in show_player:
        if i == 11:
            show_player[show_player.index(i)] = "A"
    for i in show_dealer:
        if i == 11:
            show_dealer[show_dealer.index(i)] = "A"

    for i in range(1, len(show_dealer)):
        show_dealer[i] = "?"

    print(f"Dealer's cards: {show_dealer}")
    print(f"Your cards: {show_player}")


def end_display_card():
    show_player = player_hand.copy()
    show_dealer = dealer_hand.copy()

    for i in show_player:
        if i == 11:
            show_player[show_player.index(i)] = "A"
    for i in show_dealer:
        if i == 11:
            show_dealer[show_dealer.index(i)] = "A"

    print(f"Dealer's cards: {show_dealer}")
    print(f"Your cards: {show_player}")


def turn():
    user_input = input("Do you wish to hit or stand (""h"" for hit, any key for stand): ")

    player_stand = False
    if user_input == "h":
        player_hand.append(random.choice(cards))
    else:
        player_stand = True
        print("You chose to stand")

    if sum_dealer < 17:
        dealer_hand.append(random.choice(cards))

    return player_stand


# start game
print("Blackjack 1.0v")

# deal cards
for i in range(0, 2):
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

player_stand = False
while not player_stand:
    # count player's hand
    sum_player = sum(player_hand)
    if (11 in player_hand) and (sum_player > 21):
        sum_player -= 10

    # count dealer's hand
    sum_dealer = sum(dealer_hand)
    if (11 in dealer_hand) and (sum_dealer > 21):
        sum_player -= 10

    display_card()

    if sum_dealer > 21:
        end_display_card()
        print(f"Dealer has {sum_dealer}, You win.")
        passed = True
        break
    elif sum_player > 21:
        end_display_card()
        print(f"You have {sum_player}, Dealer wins.")
        passed = True
        break

    player_stand = turn()

# open cards
if not passed:
    end_display_card()

    if sum_player > sum_dealer:
        print("You win.")
    elif sum_dealer > sum_player:
        print("Dealer wins.")
    else:
        print("Draw.")
