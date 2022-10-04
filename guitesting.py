import random
import pygame
import os
import constants as cnst

LOADED_IMAGES = {
    "Ace of Spades"
    "King of Spades"
    "Queen of Spades"
    "Jack of Spades"
    "Ten of Spades"
    "Nine of Spades"
    "Eight of Spades"
    "Seven of Spades"
    "Six of Spades"
    "Five of Spades"
    "Four of Spades"
    "Three of Spades"
    "Two of Spades"
    "Ace of Hearts"
    "King of Hearts"
    "Queen of Hearts"
    "Jack of Hearts"
    "Ten of Hearts"
    "Nine of Hearts"
    "Eight of Hearts"
    "Seven of Hearts"
    "Six of Hearts"
    "Five of Hearts"
    "Four of Hearts"
    "Three of Hearts"
    "Two of Hearts"
}

GAMES_LIST = ['bridge', 'snap', 'hearts'] #robustttttt

LOADED_GAMES = {
    "bridge": "bridge1.txt",
    "hearts": "hearts3.txt"
}

WELCOME_TEXT1 = "Hello and welcome to this card dealing program,"
WELCOME_TEXT2 = "please enter the required inputs here first,"
WELCOME_TEXT3 = "and then open up the created game window."
GAME_INPUT_TEXT = "Which game would you like? "
AVAILABLE_GAMES_TEXT = ""
PLAYERS_INPUT_TEXT = "How many players? "
CARDSPERPLAYER_INPUT_TEXT = "How many cards per player? "
WILDCARD_INPUT_TEXT = "Would you like to add any extra wild cards? (y/n) "
WILDCARD_QUESTION1_INPUT_TEXT = "How many wild cards? "
WILDCARD_QUESTION2_INPUT_TEXT = "What is the value of the wild cards? "
THANKYOU_TEXT = "Thank you, please now open the new window"

WIDTH, HEIGHT = 1100, 625
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Dealing")

pygame.font.init()
FONT = pygame.font.Font(None, 32)

SELECT_GAME_TEXT = FONT.render("Select Game", False, (0, 0, 0))

WHITE = (255, 255, 255)

FPS = 10

CARD_WIDTH = 54
CARD_HEIGHT = 75

CARD = pygame.image.load(os.path.join('assets', '2C.png'))
TEST_IMAGE = pygame.transform.scale(CARD, (CARD_WIDTH, CARD_HEIGHT))

list_of_card_codes = ['AS', 'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S', 'AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H', 'AD', 'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D', 'AC', 'KC', 'QC', 'JC', 'TC', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C']


def process_game_file(user_game):
    # Opens game file, makes a list of all the lines the in text file, closes the file
    game_file = open(LOADED_GAMES[user_game], "r")
    game_file_content = game_file.readlines()
    game_file.close()

    # Creates variables of the deck text file name (line 1) and number of cards in the deck (line 2)
    deck_file_name = game_file_content[0].strip()
    no_of_cards = int(game_file_content[1].strip())
    del game_file_content[0:2]

    # Makes a dictionary of cards using the Text File's card coding system
    card_naming_sys = {}
    x = -1
    for element in game_file_content:
        x += 1
        individual_card = game_file_content[x].strip().split(",")
        card_naming_sys[individual_card[0].upper()] = individual_card[1]
    
    deck_file = open(deck_file_name, "r")
    deck_file_content = deck_file.read()
    deck_file.close

    list_of_card_codes = []
    x=2
    for char in range(0, len(deck_file_content), x):
        list_of_card_codes.append(deck_file_content[char : char + x])

    return no_of_cards, card_naming_sys, list_of_card_codes



def process_inputs(list_of_card_codes, user_players, user_cardsperplayer):

    random.shuffle(list_of_card_codes)

    players = {}
    for player in range(user_players):
        name = "player"+str(player)
        players[name] = []
    
    x = -1
    for card in range(user_cardsperplayer * user_players):
        x += 1
        if x == user_players:
            x = 0
        players["player"+str(x)].append(list_of_card_codes[0].strip())
        del list_of_card_codes[0]

    players["left_overs"] = list_of_card_codes.copy()

    return players
    


def accept_inputs():
    print(WELCOME_TEXT1)
    print(WELCOME_TEXT2)
    print(WELCOME_TEXT3)
    while True:
        user_game = input(GAME_INPUT_TEXT+AVAILABLE_GAMES_TEXT)
        if user_game.lower() in GAMES_LIST:
            break
        else:
            print("Sorry that is not a loaded game, please try again")
    
    no_of_cards, card_naming_sys, list_of_card_codes = process_game_file(user_game)

    user_wildcards_number = "x" #this is so I can have something to pass to the process_input() function
    user_wildcards_value = "x" #this is so I can have something to pass to the process_input() function
    while True:
        user_wildcards = input(WILDCARD_INPUT_TEXT)
        if user_wildcards.lower() == "y" or user_wildcards.lower() == "yes":
            break
        elif user_wildcards.lower() == "n" or user_wildcards.lower() == "no":
            break
        else:
            print("Please input y or n")
    if user_wildcards == "y" or user_wildcards == "yes":
        while True:
            try:
                user_wildcards_number = int(input(WILDCARD_QUESTION1_INPUT_TEXT))
                if user_wildcards_number >= 1 and user_wildcards_number <= 10:
                    break
                else:
                    print("Please input a value between 1 and 10")
            except ValueError:
                print("Please input a value between 1 and 10")
        user_wildcards_value = input(WILDCARD_QUESTION2_INPUT_TEXT)
        for x in range(user_wildcards_number):
            list_of_card_codes.append("x"+str(x))
            no_of_cards += 1
    while True:
        try:
            user_players = int(input(PLAYERS_INPUT_TEXT))
            if user_players >= 1 and user_players <= no_of_cards:
                break
            else:
                print("Please input a value between 1 and "+str(no_of_cards))
        except ValueError:
            print("Please input a value between 1 and "+str(no_of_cards))
    while True:
        try:
            user_cardsperplayer = int(input(CARDSPERPLAYER_INPUT_TEXT))
            if user_cardsperplayer >= 1 and user_cardsperplayer <= (no_of_cards // user_players):
                break
            else:
                print("Please input a value between 1 and "+str(no_of_cards // user_players))
        except ValueError:
            print("Please input a value between 1 and "+str(no_of_cards))
    print(THANKYOU_TEXT)

    players = process_inputs(list_of_card_codes, user_players, user_cardsperplayer)  




def deal_card(temp_list):
    # if len(temp_list) == 0:
    #     temp_list = list_of_card_codes.copy()
    card = str(temp_list[0]) + ".png"
    del temp_list[0]
    return card, temp_list


def draw_window():
    WINDOW.fill(WHITE)
    WINDOW.blit(SELECT_GAME_TEXT, (860, 40))
    #WINDOW.blit(TEST_IMAGE2, (300, 100))
    x = -20
    y = 20
    temp_list = list_of_card_codes.copy() #update this obviously
    for key in range(52): #this too is something that needs to improve
        x += 60
        if x >= 820:
            x = 40
            y += 80
        card, temp_list = deal_card(temp_list)
        #image0 = pygame.image.load(os.path.join('assets', card))
        WINDOW.blit(pygame.transform.scale(pygame.image.load(os.path.join('assets', str(card))), (CARD_WIDTH, CARD_HEIGHT)), (x, y))
        #WINDOW.blit(thingg, (x, 200))
    pygame.display.update()


def main():

    accept_inputs()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()













