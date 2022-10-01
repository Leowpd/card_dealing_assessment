

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


deck_file = open(deck_file_name, "r")
deck_file_content = deck_file.read()
deck_file.close

list_of_card_codes = []
x=2
for char in range(0, len(deck_file_content), x):
    list_of_card_codes.append(deck_file_content[char : char + x])

print(list_of_card_codes)

card_code = str(input("Enter Card Code ")).upper()

card_code_li = []
x = 1   #this splits the card code every 1 digit (e.g. "AS" goes to ['A', 'S']). This may need to be improved slightly for "robustness". Maybe see what the length of a dictionary key in and set x to that (that would of course assume that all keys have the same character length).
for char in range(0, len(card_code), x):
    card_code_li.append(card_code[char : char + x])


card_name = card_naming_sys[card_code_li[0]] + " of " + card_naming_sys[card_code_li[1]]

print(card_name)




