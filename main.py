import random
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal():
    card = random.choice(cards)
    return card

def calculate_score(cards): 
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11) 
        cards.append(1)
    return sum(cards) 

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Bust, you lose"
  elif user_score == computer_score:
    return "It's a draw !"
  elif computer_score == 0:
    return "Computer's Blackjack, you lose!"
  elif user_score == 0:
    return "Blackjack, you win!"
  elif user_score > 21:
    return "Bust, You lose!"
  elif computer_score > 21:
    return "Computer bust, you win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():

    users_cards = []
    computers_cards = []
    game_over = False

    for _ in range(2):
        users_cards.append(deal())
        computers_cards.append(deal())

    while not game_over:
        user_score = calculate_score(users_cards)
        computer_score = calculate_score(computers_cards)
        print(f" Your cards: {users_cards}, current score: {user_score}")
        print(f" Computer's first card: [{computers_cards[0]}, ]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True  
        else:
            another_card = input("Do you want to hit or stand? ").lower()
            if another_card == "hit":
                users_cards.append(deal())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal())
        computer_score = calculate_score(computers_cards)
        print(f"Computer's hand: {computers_cards}")

    print(f" Your final hand: {users_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computers_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
                

while input("Welcome to Blackjack, Do you want to play: y or n? ") == "y":
    cls()
    play_game()

    







