import re

board = input('enter the game board')


def the_winner(board):
    option_1 = re.search(r'(x)...\1...\1', board)
    option_2 = re.search(r'.(x)..\1..\1.', board)
    option_3 = re.search(r'..(x)..\1..\1', board)
    option_4 = re.search(r'(x)\1\1......', board)
    option_5 = re.search(r'...(x)\1\1...', board)
    option_6 = re.search(r'......(x)\1\1', board)
    option_7 = re.search(r'(x)..\1..\1..', board)
    option_8 = re.search(r'..(x).\1.\1..', board)
    if option_1 or option_2 or option_3 or option_4 or option_5 or option_6 or option_7 or option_8:
           print('the winner is x')
           return
    option_1 = re.search(r'(o)...\1...\1', board)
    option_2 = re.search(r'.(o)..\1..\1.', board)
    option_3 = re.search(r'..(o)..\1..\1', board)
    option_4 = re.search(r'(o)\1\1......', board)
    option_5 = re.search(r'...(o)\1\1...', board)
    option_6 = re.search(r'......(o)\1\1', board)
    option_7 = re.search(r'(o)..\1..\1..', board)
    option_8 = re.search(r'..(o).\1.\1..', board)
    if option_1 or option_2 or option_3 or option_4 or option_5 or option_6 or option_7 or option_8:
        print('the winner is o')
    else:
        print('no one won')


the_winner(board)

