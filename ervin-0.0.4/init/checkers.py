#!/usr/bin/env python3

import os
import ervin_init as erv

bot = erv.Ervin()

# formatting colors
reset = "\033[0m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
BRed = "\033[1;31m"
BYellow = "\033[1;33m"
BBlue = "\033[1;34m"
BPurple = "\033[1;35m"
On_Black = "\033[40m"
BIRed = "\033[1;91m"
BIYellow = "\033[1;93m"
BIBlue = "\033[1;94m"
BIPurple = "\033[1;95m"
IWhite = "\033[0;97m"
black = "\033[0;30m"
iblack = "\033[0;90m"


p1 = f"{red}P1{reset}"
p2 = f"{blue}P2{reset}"
p1k = "p1k"
p2k = "p2k"
p1l = [p1, p1k]
p2l = [p2, p2k]

# Default board reference
d_board = ["0", "1", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "11", "12", "13", "14", "15",
           "16", "17", "18", "19", "20", "21", "22", "23",
           "24", "25", "26", "27", "28", "29", "30", "31",
           "32", "33", "34", "35", "36", "37", "38", "39",
           "40", "41", "42", "43", "44", "45", "46", "47",
           "48", "49", "50", "51", "52", "53", "54", "55",
           "56", "57", "58", "59", "60", "61", "62", "63"]

available_spots = ["1", "3", "5", "7",
                   "8", "10", "12", "14",
                   "17", "19", "21", "23",
                   "24", "26", "28", "30",
                   "33", "35", "37", "39",
                   "40", "42", "44", "46",
                   "49", "51", "53", "55",
                   "56", "58", "60", "62"]

# Realtime board and reset
board = ["0", p2, "2", p2, "4", p2, "6", p2,
          p2, "9", p2, "11", p2, "13", p2, "15",
          "16", p2, "18", p2, "20", p2, "22", p2,
          "24", "25", "26", "27", "28", "29", "30", "31",
          "32", "33", "34", "35", "36", "37", "38", "39",
          p1, "41", p1, "43", p1, "45", p1, "47",
          "48", p1, "50", p1, "52", p1, "54", p1,
          p1, "57", p1, "59", p1, "61", p1, "63"]

# TESTING BOARD
boardr = ["0", "1", "2", "3", "4", "5", "6", "7",
           "8", "9", p2, "11", "12", "13", "14", "15",
           "16", "17", "18", "19", "20", "21", "22", "23",
           "24", "25", "26", "27", "28", "29", "30", "31",
           "32", p1, "34", p1, "36", "37", "38", "39",
           p1, "41", p1, "43", p1, "45", "46", "47",
           "48", "49", "50", "51", "52", "53", "54", "55",
           "56", "57", "58", "59", "60", "61", "62", "63"]


def display_board():
    b = []
    p1_pieces = [each for each in board if each in p1l]
    p1_pieces = len(p1_pieces)
    p2_pieces = [each for each in board if each in p2l]
    p2_pieces = len(p2_pieces)
    spaces = " " * ((p1_pieces < 10) + (p2_pieces < 10))
    for index, each in enumerate(board):
        os.system('cls' if os.name == 'nt' else 'clear')

        color2 = purple # available_pieces color
        color3 = yellow # selected piece color
        if each == p1:
            color = red
        elif each == p2:
            color = blue
        elif each == p1k:
            color = BIRed
            color2 = BIPurple
            color3 = BIYellow
        elif each == p2k:
            color = BIBlue
            color2 = BIPurple
            color3 = BIYellow
        elif each.isdigit() and each in available_spots:
            color = iblack  # available squares
        else:
            color = black  # unused squares
        if index < 10:
            findex = f"0{index}"
        else:
            findex = f"{index}"

        if selection_process is True:
            if index in available_pieces:
                b.append(f"{color}[{color2}{findex}{color}]")
            else:
                b.append(f"{color}[{findex}]")
        elif cord_process is True:
            if index == int(selection):
                b.append(f"{color}[{color3}{findex}{color}]")
            elif index in available_cords:
                b.append(f"{iblack}[{green}{findex}{iblack}]")
            else:
                b.append(f"{color}[{findex}]")
        else:
            b.append(f"{color}[{findex}]")
    print(f"""
{On_Black}                                    {reset}
{On_Black}  {reset} {current_player}{reset}'s turn.              {spaces}{red}{p1_pieces}{reset} - {blue}{p2_pieces}{On_Black}  {reset}                     
{On_Black}                                    {reset}
{On_Black}  {b[0]}{b[1]}{b[2]}{b[3]}{b[4]}{b[5]}{b[6]}{b[7]}{On_Black}  {reset}
{On_Black}  {b[8]}{b[9]}{b[10]}{b[11]}{b[12]}{b[13]}{b[14]}{b[15]}{On_Black}  {reset}
{On_Black}  {b[16]}{b[17]}{b[18]}{b[19]}{b[20]}{b[21]}{b[22]}{b[23]}{On_Black}  {reset}
{On_Black}  {b[24]}{b[25]}{b[26]}{b[27]}{b[28]}{b[29]}{b[30]}{b[31]}{On_Black}  {reset}
{On_Black}  {b[32]}{b[33]}{b[34]}{b[35]}{b[36]}{b[37]}{b[38]}{b[39]}{On_Black}  {reset}
{On_Black}  {b[40]}{b[41]}{b[42]}{b[43]}{b[44]}{b[45]}{b[46]}{b[47]}{On_Black}  {reset}
{On_Black}  {b[48]}{b[49]}{b[50]}{b[51]}{b[52]}{b[53]}{b[54]}{b[55]}{On_Black}  {reset}
{On_Black}  {b[56]}{b[57]}{b[58]}{b[59]}{b[60]}{b[61]}{b[62]}{b[63]}{On_Black}  {reset}
{On_Black}                                    {reset}""")


def space_empty(direction, pos):
    # is the space corresponding to the pawn empty?
    directions = {"up_right": -7, "up_left": -9, "down_right": 9, "down_left": 7, "2up_right": -14, "2up_left": -18, "2down_right": 18, "2down_left": 14}
    direction_number = directions[direction]
    pos = int(pos)
    if str(pos + direction_number) in available_spots and board[pos + direction_number] in available_spots:
        return True
    return False


def space_enemy(direction, pos):
    # is the space corresponding to the pawn an enemy?
    directions = {"up_right": -7, "up_left": -9, "down_right": 9, "down_left": 7}
    direction_number = directions[direction]
    pos = int(pos)
    if board[pos] in p1l:
        enemy_list = p2l
    else:
        enemy_list = p1l
    if str(pos + direction_number) in available_spots and board[pos + direction_number] in enemy_list:
        return True
    return False


def can_eat(pos):
    pos = int(pos)
    if str(pos) not in available_spots:
        return False
    if board[pos] in p1l or is_king(pos):
        if space_enemy("up_right", pos) and space_empty("2up_right", pos):
            return True
        if space_enemy("up_left", pos) and space_empty("2up_left", pos):
            return True

    if board[pos] in p2l or is_king(pos):
        if space_enemy("down_left", pos) and space_empty("2down_left", pos):
            return True
        if space_enemy("down_right", pos) and space_empty("2down_right", pos):
            return True
    return False


def can_move(pos):
    pos = int(pos)
    if str(pos) not in available_spots:
        return False
    if can_eat(pos):
        return True
    if space_empty("up_right", pos) or space_empty("up_left", pos):
        if board[pos] in p1l or is_king(pos):
            return True
    if space_empty("down_right", pos) or space_empty("down_left", pos):
        if board[pos] in p2l or is_king(pos):
            return True
    return False


def does_list_have_eaters(list_):
    for each in list_:
        if can_eat(each):
            return True
    return False


selection = ''
selection_process = False
available_pieces = []
def select_pawn():
    global selection_process, available_pieces, selection
    available_pieces = [index for index, each in enumerate(board) if each in current_player_list and can_move(index)]
    if force_eat is True and does_list_have_eaters(available_pieces):
        for each in available_pieces[:]:
            if not can_eat(each):
                available_pieces.remove(each)

    selection_process = True
    display_board()
    selection = input(f"{current_player} select a piece. Available pieces: {purple}{available_pieces}{reset} ")
    while True:
        if not selection.isdigit():
            selection = input(f"Invalid input. Possible options: {purple}{available_pieces}{reset} Try again: ")
            continue
        if int(selection) not in available_pieces:
            selection = input(f"Invalid input. Possible options: {purple}{available_pieces}{reset} Try again: ")
            continue
        else:
            break
    selection = selection.lstrip('0')
    selection_process = False


cord_process = False
available_cords = []
def select_cord():
    global board, selection, cord_process, available_cords
    # creating a list with the only possible cordinates the selected piece can go:
    double_jump = False
    while True:
        cord = None
        available_cords = []
        if not (force_eat is True and can_eat(selection)) and (double_jump is False):
            if current_player == p1 or is_king(selection):
                if space_empty("up_right", selection):
                    available_cords.append(int(selection) - 7)
                if space_empty("up_left", selection):
                    available_cords.append(int(selection) - 9)
            if current_player == p2 or is_king(selection):
                if space_empty("down_left", selection):
                    available_cords.append(int(selection) + 7)
                if space_empty("down_right", selection):
                    available_cords.append(int(selection) + 9)
        if can_eat(selection):
            if current_player == p1 or is_king(selection):
                if space_empty("2up_right", selection) and space_enemy("up_right", selection):
                    available_cords.append(int(selection) - 14)
                if space_empty("2up_left", selection) and space_enemy("up_left", selection):
                    available_cords.append(int(selection) - 18)
            if current_player == p2 or is_king(selection):
                if space_empty("2down_left", selection) and space_enemy("down_left", selection):
                    available_cords.append(int(selection) + 14)
                if space_empty("2down_right", selection) and space_enemy("down_right", selection):
                    available_cords.append(int(selection) + 18)
        available_cords.sort()

        # starting the cord_process, choosing a cord the piece will move to.
        cord_process = True
        display_board()
        if double_jump is False:
            print(f"{current_player} selected piece at {yellow}{selection}{reset}.")
        cord = input(f"Select a coordinate to go to: ")
        while True:
            cord = cord.lstrip('0')
            if not cord.isdigit() or cord not in available_spots:
                cord = input(f"Invalid coordinate. Available coordinates: {green}{available_cords}{reset}. Try again: ")
                continue
            elif int(cord) not in available_cords:
                cord = input(f"Invalid coordinate. Available coordinates: {green}{available_cords}{reset}. Try again: ")
                continue
            else:
                break

        # capturing pieces
        captured_piece = None
        if int(cord) < int(selection) - 10 or int(cord) > int(selection) + 10:
            if current_player == p1 or is_king(selection):
                if int(cord) == int(selection) - 14:
                    captured_piece = int(selection) - 7
                elif int(cord) == int(selection) - 18:
                    captured_piece = int(selection) - 9
            if current_player == p2 or is_king(selection):
                if int(cord) == int(selection) + 14:
                    captured_piece = int(selection) + 7
                elif int(cord) == int(selection) + 18:
                    captured_piece = int(selection) + 9

        if captured_piece is not None:
            board[captured_piece] = d_board[captured_piece]

        if current_player == p1 and not is_king(selection) and board[int(cord)] in ["1", "3", "5", "7"]:
            board[int(cord)] = p1k
        elif current_player == p2 and not is_king(selection) and board[int(cord)] in ["56", "58", "60", "62"]:
            board[int(cord)] = p2k
        else:
            board[int(cord)] = board[int(selection)]

        board[int(selection)] = d_board[int(selection)]
        if captured_piece is None:
            if current_player == p1:
                print(f"Pawn {red}{selection}{reset} moved to square {green}{cord}{reset} without capturing any pieces.")
            elif current_player == p2:
                print(f"Pawn {blue}{selection}{reset} moved to square {green}{cord}{reset} without capturing any pieces.")
        else:
            if current_player == p1:
                print(
                    f"Pawn {red}{selection}{reset} moved to square {green}{cord}{reset} and captured: {blue}{captured_piece}{reset}")
            elif current_player == p2:
                print(
                    f"Pawn {blue}{selection}{reset} moved to square {green}{cord}{reset} and captured: {red}{captured_piece}{reset}")
        if can_eat(cord) and captured_piece is not None:
            if force_eat is False:
                input1 = None
                selection = cord
                available_cords = []
                if current_player == p1 or is_king(selection):
                    if space_empty("2up_right", selection) and space_enemy("up_right", selection):
                        available_cords.append(int(selection) - 14)
                    if space_empty("2up_left", selection) and space_enemy("up_left", selection):
                        available_cords.append(int(selection) - 18)
                if current_player == p2 or is_king(selection):
                    if space_empty("2down_left", selection) and space_enemy("down_left", selection):
                        available_cords.append(int(selection) + 14)
                    if space_empty("2down_right", selection) and space_enemy("down_right", selection):
                        available_cords.append(int(selection) + 18)
                available_cords.sort()
                display_board()
                while input1 not in ["yes", "no"]:
                    input1 = input("Do you want to continue capturing? (yes, no): ")
                if input1 == "yes":
                    double_jump = True
                    continue
                else:
                    break
            else:
                print("You are forced to capture again.")
                double_jump = True
                selection = cord
                continue
        else:
            break
    cord_process = False


def is_king(pawn):
    pawn = int(pawn)
    if d_board[pawn] not in available_spots:
        return False
    if board[pawn] == p1k or board[pawn] == p2k:
        return True
    return False


def check_for_win():
    global winner, game_is_active
    p1_list = []
    p2_list = []
    for index, each in enumerate(board):
        if each in p1l:
            p1_list.append(index)
        if each in p2l:
            p2_list.append(index)
    if p1_list == []:
        winner = p2
        game_is_active = False
    elif p2_list == []:
        winner = p1
        game_is_active = False
    else:
        p1_can_move = 0
        p2_can_move = 0
        for each in p1_list:
            if can_move(each):
                p1_can_move = 1
        for each in p2_list:
            if can_move(each):
                p2_can_move = 1
        if p1_can_move == 0:
            winner = p2
            game_is_active = False
        elif p2_can_move == 0:
            winner = p1
            game_is_active = False


def switch_player():
    global current_player, current_player_list
    if current_player == p1:
        current_player = p2
        current_player_list = p2l
    else:
        current_player = p1
        current_player_list = p1l

           
# start of game
winner = None
force_eat = False
game_is_active = True
current_player = p1
current_player_list = p1l
while game_is_active:
    select_pawn()
    select_cord()
    check_for_win()
    switch_player()
display_board()
print(f"{winner} {reset}has won the game.")
