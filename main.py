# Opens game file, makes a list of all the lines the in text file, closes the file
game_file = open("bridge1.txt", "r")
game_file_content = game_file.readlines()
game_file.close()

# Creates variables of the deck text file name (line 1) and number of cards in the deck (line 2)
deck_file_name = game_file_content[0].strip()
no_of_cards = game_file_content[1].strip()

# Removes the first two elements of the game_file_content list (i.e. the deck file name and number of cards - the stuff we've already got)
del game_file_content[0:2]

# Makes a dictionary of cards using the Text File's card coding system
card_naming_sys = {}
x = -1
for element in game_file_content:
    x += 1
    individual_card = game_file_content[x].strip().split(",")
    card_naming_sys[individual_card[0].upper()] = individual_card[1]

print(card_naming_sys)