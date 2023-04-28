from random import choice
from string import ascii_lowercase
from time import sleep
import os
from msvcrt import getch
   


hangmanpic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


alphabet = list(ascii_lowercase)


with open('word.txt', 'r') as f:
    wordlist = f.readlines()
    





def credit() :
    os.system('CLS')
    print('   ___________.._______                                           ')
    print('  | .__________))______|')
    print('  | | / /      ||                  _____                          ')
    print('  | |/ /       ||                 |  |  |___ ___ ___ _____ ___ ___')
    print('  | | /        ||.-``.            |     | .`|   | . |     | .`|   |')
    print('  | |/         |/  _  \           |__|__|__,|_|_|_  |_|_|_|__,|_|_|')
    print('  | |          ||  `/,|                         |___|              ')
    print('  | |          (\\`_.`                                             ')
    print('  | |         .-`--`.                                              ')
    print('  | |        /Y . . Y\                Press C to Play              ')
    print('  | |       // |   | \\               Press Q to Quit              ')
    print('  | |      //  | . |  \\              Press R to Credit            ')
    print('  | |     `)   |   |   (`                                          ')
    print('  | |          ||`||                                               ')
    print('  | |          || ||                                               ')
    print('  | |          || ||                  Author: Saccarose            ')
    print("  | |          || ||                                               ")
    print("  | |         / | | \                                              ")
    print('  """"""""""|_`-` `-` |"""|					      ')
    print('  |"|"""""""\ \       `"|"|                                        ')
    print('  | |        \ \        | |					      ')
    print('  : :         \ \       : :                                        ')
    print('  . .          ``       . .                                        ')



def end():
    os.system('CLS')
    print("Press C to play again")
    print("Press Q to menu")
    while True:
        input_key = ord(getch())
        
        if input_key==99:
            gotogame=True
            break
        if input_key==113:
            gotogame="start"
            break
    if gotogame=="start":
        start()
    if gotogame==True:
        main()


def main():
    os.system('CLS')
    global output, count, pic
    count=0
    
    word = choice(wordlist).strip()
    length = len(word)
    output_list = ["_"] * length
    output = "".join(output_list)


    print("This word has", length, "letter")
    print(output)
    while True:
        myletter = input().lower()
        
        if len(myletter) != 1 or myletter not in alphabet:
            os.system('CLS')
            print(output)
            if count !=0:
                print(hangmanpic[count-1])
            print("Invalid input. Please try again.")
        
            continue
        
        if myletter in word:
            for i in range(length):
                if myletter == word[i]:
                    output_list[i] = myletter
            output = "".join(output_list)
            os.system('CLS')
            print(output)
            if count !=0:
                print(hangmanpic[count-1])
            
        else:
            os.system('CLS')
            print(output)
            count+=1
            
            if count!=7: print(hangmanpic[count-1])
            
            else:
                print(hangmanpic[6])
                print("You lose! The word is", word); break
        if output == word:
            os.system('CLS')
            print("Congratulations! The word is", word)
            break
    print("Press Enter to continue...")
    i = input()
    end()


def start():
    os.system('CLS')
    print('   ___________.._______                                           ')
    print('  | .__________))______|')
    print('  | | / /      ||                  _____                          ')
    print('  | |/ /       ||                 |  |  |___ ___ ___ _____ ___ ___')
    print('  | | /        ||.-``.            |     | .`|   | . |     | .`|   |')
    print('  | |/         |/  _  \           |__|__|__,|_|_|_  |_|_|_|__,|_|_|')
    print('  | |          ||  `/,|                         |___|               ')
    print('  | |          (\\`_.`                                             ')
    print('  | |         .-`--`.                                              ')
    print('  | |        /Y . . Y\                Press C to Play              ')
    print('  | |       // |   | \\               Press Q to Quit              ')
    print('  | |      //  | . |  \\              Press R to Credit            ')
    print('  | |     `)   |   |   (`                                          ')
    print('  | |          ||`||                                               ')
    print('  | |          || ||                                               ')
    print('  | |          || ||                                               ')
    print("  | |          || ||                                               ")
    print("  | |         / | | \                                              ")
    print('  """"""""""|_`-` `-` |"""|					      ')
    print('  |"|"""""""\ \       `"|"|                                        ')
    print('  | |        \ \        | |					      ')
    print('  : :         \ \       : :                                        ')
    print('  . .          ``       . .                                        ')
    
    while True:
        input_key = ord(getch())
        
        if input_key==99:
            gotogame=True
            break
        if input_key==113:
            gotogame=False
            break
        if input_key == 114:
            credit()
    if gotogame==True:
        main()
start()
