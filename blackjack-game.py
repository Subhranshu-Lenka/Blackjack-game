import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

      """


def hit_card():
    """Returns a random card"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card


def game(cur_amount):
    while(True):
        try:
            bid_amount = int(input('Enter the bidding amount  '))
            print()
            if(bid_amount <= 0):
                raise ValueError("Bidding amount can't be zero or negative !!")
            if(bid_amount > cur_amount):
                raise ValueError(
                    "You can't bid higher than your current balance!!")
            break
        except:

            print('You entered an invalid amount')

    # Player cards
    player = []

    # computer card
    computer = []

    for i in range(3):
        new_card = hit_card()
        if(i < 2):
            player.append(new_card)
        else:
            computer.append(new_card)

    print(f"    Your starting cards {player}     current score {sum(player)}")
    print(f"    Computer's starting cards {computer[0]} ")

    stand = False
    while(sum(player) < 21 and stand != True):
        player_choose = input(
            "Type 'y' to hit a new card or Type 'n' to hold your position ").lower()
        if(player_choose == 'y'):
            new_card = hit_card()
            player.append(new_card)
            print(f"    Your cards {player}     current score {sum(player)}")
        elif (player_choose == 'n'):
            stand = True
        else:
            continue

    player_card_sum = sum(player)

    stand = False
    while(sum(computer) < 21 and stand != True and player_card_sum < 22):
        comp_card_sum = sum(computer)

        if(comp_card_sum < player_card_sum and comp_card_sum < 15):
            new_card = hit_card()
            computer.append(new_card)
            print(
                f"    Computer's card {computer}     current score {sum(computer)}")
        elif (comp_card_sum < player_card_sum and comp_card_sum >= 15):
            comp_choice = random.randrange(1, 10)
            if comp_choice > 5:
                new_card = hit_card()
                computer.append(new_card)
                print(
                    f"    Computer's card {computer}     current score {sum(computer)}")
            else:
                stand = True
        else:
            stand = True

    comp_card_sum = sum(computer)

    print()
    print(f"Computer's Cards {computer}     Player's Cards {player}")

    # winner selection
    if(comp_card_sum == player_card_sum):
        print("\___-----PUSH-----___/ \nComputer and you score same!!")
    elif(player_card_sum > 21):
        print('\___Computer Won___/ \nYou went over 21')
        cur_amount -= bid_amount
    elif(comp_card_sum > 21):
        print('\___You Won___/ \nComputer went over 21')
        cur_amount -= bid_amount
    elif(player_card_sum > comp_card_sum):
        print('\___You Won___/')
        cur_amount += bid_amount
    else:
        print('\___Computer Won___/')
        cur_amount -= bid_amount
    return cur_amount


print(logo)
print('Welcome to the Blackjack Game!!')
starting_amount = 1000
print()
while(True):
    start = input(
        f'Your current balance is {starting_amount}. Choose "Y" to play  "N" to quit. \t').lower()
    if start == 'y':
        starting_amount = game(starting_amount)
        if(starting_amount <= 0):
            print("You went and lost everything 😥😖 \nGo and come again later!!")
            break
    else:
        print("Thank you to finding us!! \nBye✋Have a great day ✨")
        break
