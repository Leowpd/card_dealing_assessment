import random
import pygame
import os
import constants as cnst


WINDOW = pygame.display.set_mode((cnst.WINDOW_WIDTH, cnst.WINDOW_HEIGHT))
pygame.display.set_caption("Card Dealing")
pygame.font.init()
FONT = pygame.font.Font(None, 32)

IMAGE1 = pygame.image.load(os.path.join('assets', 'instructions_english.png'))
IMAGE2 = pygame.image.load(os.path.join('assets', 'instructions_maori.png'))
IMAGE3 = pygame.image.load(os.path.join('assets', 'cards_error_english.png'))
IMAGE4 = pygame.image.load(os.path.join('assets', 'cards_error_maori.png'))

INSTRUCTIONS_ENGLISH = pygame.transform.scale(IMAGE1, \
    (cnst.INSTRUCTIONS_WIDTH, cnst.INSTRUCTIONS_HEIGHT))
INSTRUCTIONS_MAORI = pygame.transform.scale(IMAGE2, \
    (cnst.INSTRUCTIONS_WIDTH, cnst.INSTRUCTIONS_HEIGHT))
CARDS_ERROR_ENGLISH = pygame.transform.scale(IMAGE3, \
    (cnst.CARDS_ERROR_WIDTH, cnst.CARDS_ERROR_HEIGHT))
CARDS_ERROR_MAORI = pygame.transform.scale(IMAGE4, \
    (cnst.CARDS_ERROR_WIDTH, cnst.CARDS_ERROR_HEIGHT))


#processes the game file
def process_game_file(user_game):
    game_file = open(cnst.LOADED_GAMES[user_game], "r")
    game_file_content = game_file.readlines()
    game_file.close()

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
    y = 2
    for char in range(0, len(deck_file_content), y):
        card_code = deck_file_content[char : char + y]
        card_code_li = []
        x = 1   #this splits the card code (e.g. "AS" goes to ['A', 'S']).
        for char in range(0, len(card_code), x):
            card_code_li.append(card_code[char : char + x])

        list_of_card_codes.append(card_naming_sys[card_code_li[0]] + \
            " of " + card_naming_sys[card_code_li[1]])

    return no_of_cards, card_naming_sys, list_of_card_codes


#processes player inputs
def process_inputs(list_of_card_codes, user_players, user_cardsperplayer):
    random.shuffle(list_of_card_codes)
    players = {}
    player_names = []
    for player in range(user_players):
        name = "player" + str(player)
        players[name] = []
        player_names.append(name)
    
    x = -1
    for card in range(user_cardsperplayer * user_players):
        x += 1
        if x == user_players:
            x = 0
        players["player" + str(x)].append(list_of_card_codes[0].strip())
        del list_of_card_codes[0]
        
    return players, player_names


#accepts and verifies player inputs
def accept_inputs():
    print(cnst.TEXTS["WELCOME_TEXT"])
    while True:
        user_language = input(cnst.TEXTS["LANGUAGE_INPUT_TEXT"]).lower()
        if user_language == "1" or user_language == "one" \
            or user_language == "english":
            user_language = "ENGLISH"
            break
        elif user_language == "2" or user_language == "two" or \
            user_language == "te reo maori" or user_language == "te reo māori"\
                or user_language == "te reo" or user_language == "māori" \
                    or user_language == "maori":
            user_language = "MAORI"
            break
    while True:
        user_game = input(cnst.TEXTS[str(user_language) + \
            "_GAME_INPUT_TEXT"] + cnst.GAMES)
        if user_game.lower() in cnst.GAMES_LIST:
            break
        else:
            print(cnst.TEXTS[str(user_language) + "_GAME_ERROR_TEXT"])
    
    no_of_cards, card_naming_sys, list_of_card_codes \
        = process_game_file(user_game)

    user_wildcards_number = "#%" #something to pass to process_input()
    user_wildcards_value = "#%" #something to pass to process_input()
    while True:
        user_wildcards = input(cnst.TEXTS[str(user_language) + \
            "_WILDCARD_INPUT_TEXT"])
        if user_wildcards.lower() == "y" \
            or user_wildcards.lower() == "yes":
            break
        elif user_wildcards.lower() == "n" \
            or user_wildcards.lower() == "no":
            break
        else:
            print(cnst.TEXTS[str(user_language) + "_WILDCARDS_ERROR_TEXT"])
    if user_wildcards == "y" or user_wildcards == "yes":
        while True:
            try:
                user_wildcards_number = int(input(cnst.TEXTS\
                    [str(user_language) + "_WILDCARD_QUESTION1_INPUT_TEXT"]))
                if user_wildcards_number >= 1 and user_wildcards_number <= 10:
                    break
                else:
                    print(cnst.TEXTS[str(user_language) + \
                        "_NUMBER_INPUT_ERROR"] + "10")
            except ValueError:
                print(cnst.TEXTS[str(user_language) + \
                    "_NUMBER_INPUT_ERROR"] + "10")
        user_wildcards_value = input(cnst.TEXTS[str(user_language) + \
            "_WILDCARD_QUESTION2_INPUT_TEXT"])
        for x in range(user_wildcards_number):
            list_of_card_codes.append("Wildcard " + str(x + 1))
            no_of_cards += 1
    while True:
        try:
            user_players = int(input(cnst.TEXTS[str(user_language) + \
                "_PLAYERS_INPUT_TEXT"]))
            if user_players >= 1 and user_players <= no_of_cards:
                break
            else:
                print(cnst.TEXTS[str(user_language) + "_NUMBER_INPUT_ERROR"] \
                    + str(no_of_cards))
        except ValueError:
            print(cnst.TEXTS[str(user_language) + "_NUMBER_INPUT_ERROR"] + \
                str(no_of_cards))
    while True:
        try:
            user_cardsperplayer = int(input(cnst.TEXTS[str(user_language) + \
                "_CARDSPERPLAYER_INPUT_TEXT"]))
            if user_cardsperplayer >= 1 and user_cardsperplayer <= \
                (no_of_cards // user_players):
                break
            else:
                print(cnst.TEXTS[str(user_language) + "_NUMBER_INPUT_ERROR"] \
                    + str(no_of_cards // user_players))
        except ValueError:
            print(cnst.TEXTS[str(user_language) + "_NUMBER_INPUT_ERROR"] \
                + str(no_of_cards // user_players))
    print(cnst.TEXTS[str(user_language) + "_THANKYOU_TEXT"])

    players, player_names = process_inputs(list_of_card_codes, \
        user_players, user_cardsperplayer)
    return players, player_names, user_language, user_wildcards_value


#deals a card to draw on the window
def deal_card(temp_list):
    card = cnst.LOADED_IMAGES[str(temp_list[0])]
    del temp_list[0]
    return card, temp_list


#deals with the GUI
def draw_window(players, player_names, user_language, user_wildcards_value):
    WINDOW.fill(cnst.WINDOW_COLOUR)
    if user_language == "MAORI":
        WINDOW.blit(INSTRUCTIONS_MAORI, (870, 40))
        if user_wildcards_value != "#%":
            WINDOW.blit(FONT.render\
                ("Kaari mohoao: ", False, (0, 0, 0)), (870, 540))
            WINDOW.blit(FONT.render('"' + str(user_wildcards_value) \
                + '"', False, (0, 0, 0)), (880, 565))   
    else:
        WINDOW.blit(INSTRUCTIONS_ENGLISH, (870, 40))
        if user_wildcards_value != "#%":
            WINDOW.blit(FONT.render\
                ("Wildcards: ", False, (0, 0, 0)), (870, 540))
            WINDOW.blit(FONT.render('"' + str(user_wildcards_value) \
                + '"', False, (0, 0, 0)), (880, 565)) 
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
            WINDOW.blit(pygame.transform.scale(pygame.image.load\
                (os.path.join('assets', str(card))), \
                    (cnst.CARD_WIDTH, cnst.CARD_HEIGHT)), (x, y))

    pygame.display.update()


#main function
def main():
    players, player_names, user_language, \
        user_wildcards_value = accept_inputs()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(cnst.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(players, player_names, user_language, user_wildcards_value)
    
    pygame.quit()


if __name__ == "__main__":
    main()

