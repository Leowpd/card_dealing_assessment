import random
import pygame
import os


GAMES_LIST = ['bridge', 'snap', 'hearts'] #robustttttt

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

WHITE = (255, 255, 255)

FPS = 10

CARD_WIDTH = 54
CARD_HEIGHT = 75

CARD = pygame.image.load(os.path.join('assets', '2C.png'))
TEST_IMAGE = pygame.transform.scale(CARD, (CARD_WIDTH, CARD_HEIGHT))

list_of_card_codes = ['AS', 'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S', 'AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H', 'AD', 'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D', 'AC', 'KC', 'QC', 'JC', 'TC', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C']


def deal_card(temp_list):
    # if len(temp_list) == 0:
    #     temp_list = list_of_card_codes.copy()
    card = str(temp_list[0]) + ".png"
    del temp_list[0]
    return card, temp_list


def draw_window():
    WINDOW.fill(WHITE)
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
    print(WELCOME_TEXT1)
    print(WELCOME_TEXT2)
    print(WELCOME_TEXT3)
    while True:
        user_game = input(GAME_INPUT_TEXT+AVAILABLE_GAMES_TEXT)
        if user_game.lower() in GAMES_LIST:
            break
        else:
            print("Sorry that is not a loaded game, please try again")
    while True:
        try:
            user_players = int(input(PLAYERS_INPUT_TEXT))
            if user_players >= 1 and user_players <= 52:
                break
            else:
                print("Please input a value between 1 and the 52")
        except ValueError:
            print("Please input a value between 1 and the 52")
    while True:
        try:
            user_cardsperplayer = int(input(CARDSPERPLAYER_INPUT_TEXT))
            if user_cardsperplayer >= 1 and user_cardsperplayer <= 52:
                break
            else:
                print("Please input a value between 1 and the 52")
        except ValueError:
            print("Please input a value between 1 and the 52")
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
                if user_wildcards_number >= 1 and user_wildcards_number <= 52:
                    break
                else:
                    print("Please input a value between 1 and the 52")
            except ValueError:
                print("Please input a value between 1 and the 52")
        user_wildcards_value = input(WILDCARD_QUESTION2_INPUT_TEXT)
    print(THANKYOU_TEXT)





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













