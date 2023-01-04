#!/usr/bin/env python3
import os

def term_setup(welcome, term_width, term_heght):
    os.system('cls' if os.name == 'nt' else 'clear')
    # print("\033[1;32;40m")

    # Top bar
    for i in range(0,term_width):
        if i == 0:
            print('+', end='')
            continue
        
        elif i == term_width - 1:
            print('+', end='')
            continue

        print('-', end='')

    print('')

    # Message
    for i in range(0, ((int)(term_width/2) - (int)(len(welcome)/2))):
        if i == 0:
            print('|', end='')
            continue
        
        print(" ", end='')

    print(welcome, end = '')

    for i in range(0, (int)(term_width/2) - ((int)(len(welcome)/2))):
        if i == ((int)(term_width/2) - ((int)(len(welcome)/2))) - 1:
            print('|\n', end='')
            continue
        
        print(" ", end='')
    
    # print('')

    # Bottom Bar
    for j in range(0,term_width):
        if j == 0:
            print('+', end='')
            continue
        
        elif j == term_width - 1:
            print('+', end='')
            continue

        print('-', end='')

    print('')
