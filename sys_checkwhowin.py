# color set
import str_lang as sl

def check_whowin(board):

    colored_row = []

    for row in board:
        if '將' in row:
            sl.c_label_print("bwin ","B")
        if '帥' in row:
            sl.c_label_print("rwin ","R")

    print(''.join(colored_row))