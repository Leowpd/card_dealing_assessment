import random
import pygame
import os

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













