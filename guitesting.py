import random
import pygame
import os
import constants as cnst


GAMES_LIST = ['bridge', 'hearts'] #robustttttt

LOADED_GAMES = {
    "bridge": "bridge1.txt",
    "hearts": "hearts3.txt"
}

WELCOME_TEXT1 = "Hello and welcome to this card dealing program,"
WELCOME_TEXT2 = "please enter the required inputs here first,"
WELCOME_TEXT3 = "and then open up the created game window."

LANGUAGE_INPUT_TEXT = "English (1) or Te Reo Māori (2) "


# ENGLISH_GAME_INPUT_TEXT = "Which game would you like? "
# ENGLISH_AVAILABLE_GAMES_TEXT = ""
# ENGLISH_PLAYERS_INPUT_TEXT = "How many players? "
# ENGLISH_CARDSPERPLAYER_INPUT_TEXT = "How many cards per player? "
# ENGLISH_WILDCARD_INPUT_TEXT = "Would you like to add any extra wild cards? (y/n) "
# ENGLISH_WILDCARD_QUESTION1_INPUT_TEXT = "How many wild cards? "
# ENGLISH_WILDCARD_QUESTION2_INPUT_TEXT = "What is the value of the wild cards? "

# ENGLISH_THANKYOU_TEXT = "Thank you, please now open the new window"


# MAORI_GAME_INPUT_TEXT = "Ko tehea keemu ka pirangi koe? "
# MAORI_PLAYERS_INPUT_TEXT = "Tokohia nga kaitakaro? "
# MAORI_CARDSPERPLAYER_INPUT_TEXT = "E hia nga kaari mo ia kaitakaro? "
# MAORI_WILDCARD_INPUT_TEXT = "Kei te pirangi koe ki te taapiri i etahi atu kaari mohoao? (y/n) "
# MAORI_WILDCARD_QUESTION1_INPUT_TEXT = "E hia nga kaari mohoao? "
# MAORI_WILDCARD_QUESTION2_INPUT_TEXT = "He aha te uara o nga kaari mohoao? "

# MAORI_THANKYOU_TEXT = "Tena koe, whakatuwheratia te matapihi hou inaianei"




WIDTH, HEIGHT = 1100, 625
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Dealing")

pygame.font.init()
FONT = pygame.font.Font(None, 32)

WHITE = (255, 255, 255)

FPS = 1

CARD_WIDTH = 54
CARD_HEIGHT = 75

INSTRUCTIONS_WIDTH = 180
INSTRUCTIONS_HEIGHT = 380

CARDS_ERROR_WIDTH = 180
CARDS_ERROR_HEIGHT = 68

CARD = pygame.image.load(os.path.join('assets', '2C.png'))
TEST_IMAGE = pygame.transform.scale(CARD, (CARD_WIDTH, CARD_HEIGHT))

IMAGE1 = pygame.image.load(os.path.join('assets', 'instructions_english.png'))
IMAGE2 = pygame.image.load(os.path.join('assets', 'instructions_maori.png'))
IMAGE3 = pygame.image.load(os.path.join('assets', 'cards_error_english.png'))
IMAGE4 = pygame.image.load(os.path.join('assets', 'cards_error_maori.png'))

INSTRUCTIONS_ENGLISH = pygame.transform.scale(IMAGE1, (INSTRUCTIONS_WIDTH, INSTRUCTIONS_HEIGHT))
INSTRUCTIONS_MAORI = pygame.transform.scale(IMAGE2, (INSTRUCTIONS_WIDTH, INSTRUCTIONS_HEIGHT))
CARDS_ERROR_ENGLISH = pygame.transform.scale(IMAGE3, (CARDS_ERROR_WIDTH, CARDS_ERROR_HEIGHT))
CARDS_ERROR_MAORI = pygame.transform.scale(IMAGE4, (CARDS_ERROR_WIDTH, CARDS_ERROR_HEIGHT))

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
    player_names = []
    for player in range(user_players):
        name = "player"+str(player)
        players[name] = []
        player_names.append(name)
    
    x = -1
    for card in range(user_cardsperplayer * user_players):
        x += 1
        if x == user_players:
            x = 0
        players["player"+str(x)].append(list_of_card_codes[0].strip())
        del list_of_card_codes[0]


    return players, player_names
    


def accept_inputs():
    print(WELCOME_TEXT1)
    print(WELCOME_TEXT2)
    print(WELCOME_TEXT3)

    while True:
        user_language = input(LANGUAGE_INPUT_TEXT).lower()
        if user_language == "1" or user_language == "one" or user_language == "english":
            user_language = "ENGLISH"
            break
        elif user_language == "2" or user_language == "two" or user_language == "te reo maori" or user_language == "te reo māori" or user_language == "te reo" or user_language == "māori" or user_language == "maori":
            user_language = "MAORI"
            break

    while True:
        user_game = input(cnst.TEXTS[str(user_language)+"_GAME_INPUT_TEXT"])
        if user_game.lower() in GAMES_LIST:
            break
        else:
            print(cnst.TEXTS[str(user_language)+"_GAME_ERROR_TEXT"])
    
    no_of_cards, card_naming_sys, list_of_card_codes = process_game_file(user_game)

    user_wildcards_number = "#%" #this is so I can have something to pass to the process_input() function
    user_wildcards_value = "#%" #this is so I can have something to pass to the process_input() function
    while True:
        user_wildcards = input(cnst.TEXTS[str(user_language)+"_WILDCARD_INPUT_TEXT"])
        if user_wildcards.lower() == "y" or user_wildcards.lower() == "yes":
            break
        elif user_wildcards.lower() == "n" or user_wildcards.lower() == "no":
            break
        else:
            print(cnst.TEXTS[str(user_language)+"_WILDCARDS_ERROR_TEXT"])
    if user_wildcards == "y" or user_wildcards == "yes":
        while True:
            try:
                user_wildcards_number = int(input(cnst.TEXTS[str(user_language)+"_WILDCARD_QUESTION1_INPUT_TEXT"]))
                if user_wildcards_number >= 1 and user_wildcards_number <= 10:
                    break
                else:
                    print(cnst.TEXTS[str(user_language)+"_NUMBER_INPUT_ERROR"]+"10")
            except ValueError:
                print(cnst.TEXTS[str(user_language)+"_NUMBER_INPUT_ERROR"]+"10")
        user_wildcards_value = input(cnst.TEXTS[str(user_language)+"_WILDCARD_QUESTION2_INPUT_TEXT"])
        for x in range(user_wildcards_number):
            list_of_card_codes.append("x"+str(x))
            no_of_cards += 1
    while True:
        try:
            user_players = int(input(cnst.TEXTS[str(user_language)+"_PLAYERS_INPUT_TEXT"]))
            if user_players >= 1 and user_players <= no_of_cards:
                break
            else:
                print(cnst.TEXTS[str(user_language)+"_NUMBER_INPUT_ERROR"]+str(no_of_cards))
        except ValueError:
            print(cnst.TEXTS[str(user_language)+"_NUMBER_INPUT_ERROR"]+str(no_of_cards))
    while True:
        try:
            user_cardsperplayer = int(input(cnst.TEXTS[str(user_language)+"_CARDSPERPLAYER_INPUT_TEXT"]))
            if user_cardsperplayer >= 1 and user_cardsperplayer <= (no_of_cards // user_players):
                break
            else:
                print(cnst.TEXTS[str(user_language)+"_NUMBER_INPUT_ERROR"]+str(no_of_cards // user_players))
        except ValueError:
            print(cnst.TEXTS[str(user_language)+"_NUMBER_INPUT_ERROR"]+str(no_of_cards))
    print(cnst.TEXTS[str(user_language)+"_THANKYOU_TEXT"])

    players, player_names = process_inputs(list_of_card_codes, user_players, user_cardsperplayer)
    return players, player_names, user_language, user_wildcards_value




def deal_card(temp_list):
    # if len(temp_list) == 0:
    #     temp_list = list_of_card_codes.copy()
    card = str(temp_list[0]) + ".png"
    del temp_list[0]
    return card, temp_list


def draw_window(players, player_names, user_language, user_wildcards_value):
    WINDOW.fill(WHITE)
    if user_language == "MAORI":
        WINDOW.blit(INSTRUCTIONS_MAORI, (870, 40))
        if user_wildcards_value != "#%":
            WINDOW.blit(FONT.render("Kaari mohoao: ", False, (0, 0, 0)), (870, 540))
            WINDOW.blit(FONT.render('"'+str(user_wildcards_value)+'"', False, (0, 0, 0)), (880, 565))   
    else:
        WINDOW.blit(INSTRUCTIONS_ENGLISH, (870, 40))
        if user_wildcards_value != "#%":
            WINDOW.blit(FONT.render("Wildcards: ", False, (0, 0, 0)), (870, 540))
            WINDOW.blit(FONT.render('"'+str(user_wildcards_value)+'"', False, (0, 0, 0)), (880, 565)) 
    #WINDOW.blit(TEST_IMAGE2, (300, 100))
    x = -20
    y = -100
    temp_player_names = player_names.copy()
    for player in player_names:
        x = -20
        y += 120
        temp_list = players[temp_player_names[0]].copy()
        del temp_player_names[0]
        for i in range(len(temp_list)):
            x += 60
            if x >= 820:
                x = 40
                y += 80
            if y > 550:
                if user_language == "MAORI":
                    WINDOW.blit(CARDS_ERROR_MAORI, (870, 450))
                else:
                    WINDOW.blit(CARDS_ERROR_ENGLISH, (870, 450))
                break
            card, temp_list = deal_card(temp_list)
            WINDOW.blit(pygame.transform.scale(pygame.image.load(os.path.join('assets', str(card))), (CARD_WIDTH, CARD_HEIGHT)), (x, y))



    # temp_list = list_of_card_codes.copy() #update this obviously
    # for key in range(52): #this too is something that needs to improve
    #     x += 60
    #     if x >= 820:
    #         x = 40
    #         y += 80
    #     card, temp_list = deal_card(temp_list)
    #     #image0 = pygame.image.load(os.path.join('assets', card))
    #     WINDOW.blit(pygame.transform.scale(pygame.image.load(os.path.join('assets', str(card))), (CARD_WIDTH, CARD_HEIGHT)), (x, y))
    #     #WINDOW.blit(thingg, (x, 200))


    pygame.display.update()


def main():

    players, player_names, user_language, user_wildcards_value = accept_inputs()

    print(players)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        draw_window(players, player_names, user_language, user_wildcards_value)
    
    pygame.quit()




if __name__ == "__main__":
    main()







