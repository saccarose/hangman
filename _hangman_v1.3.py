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

    
        

def credit() :
    os.system('CLS')
    print('   ___________.._______                                           ')
    print('  | .__________))______|')
    print('  | | / /      ||                  _______ _______ _______ _______ _______ _______ _______ ')
    print('  | |/ /       ||                 |   |   |   _   |    |  |     __|   |   |   _   |    |  |')
    print('  | | /        ||.-``.            |       |       |       |    |  |       |       |       |')
    print('  | |/         |/  _  \           |___|___|___|___|__|____|_______|__|_|__|___|___|__|____|')
    print('  | |          ||  `/,|                                       				')
    print('  | |          (\\`_.`                                             ')
    print('  | |         .-`--`.                                              ')
    print('  | |        /Y . . Y\                             Press C to Play              ')
    print('  | |       // |   | \\                             Press Q to Quit              ')
    print('  | |      //  | . |  \\                            Press R to Credit            ')
    print('  | |     `)   |   |   (`                                          ')
    print('  | |          ||`||                                               ')
    print('  | |          || ||                                               ')
    print('  | |          || ||                               Author: Saccarose            ')
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
    print("What topic do you want to play?")
    print("0: random topic")
    print("1: animals")
    print("")
    while True:
        input_key = ord(getch())

        if input_key == 48:
            with open('random.txt', 'r') as f:
                wordlist = f.readlines()
                break
        
        if input_key == 49:
            with open('animals.txt', 'r') as f:
                wordlist = f.readlines()
                break

        if input_key == 50:
            pass

        if input_key == 51:
            pass

        if input_key == 52:
            pass

        if input_key == 53:
            pass

        if input_key == 54:
            pass

        if input_key == 55:
            pass

        if input_key == 56:
            pass

        if input_key == 57:
            pass

        
    os.system('CLS')
    global output, count
    count = 0
    
    word = choice(wordlist).strip()
    length = len(word)
    output_list = ["_"] * length
    output = "".join(output_list)
    if cheat == True:
        print(word)
    else:
        pass

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
    global cheat
    cheat = False
    os.system('CLS')
    print('   ___________.._______                                           ')
    print('  | .__________))______|')
    print('  | | / /      ||                  _______ _______ _______ _______ _______ _______ _______ ')
    print('  | |/ /       ||                 |   |   |   _   |    |  |     __|   |   |   _   |    |  |')
    print('  | | /        ||.-``.            |       |       |       |    |  |       |       |       |')
    print('  | |/         |/  _  \           |___|___|___|___|__|____|_______|__|_|__|___|___|__|____|')
    print('  | |          ||  `/,|                                        ')
    print('  | |          (\\`_.`                                             ')
    print('  | |         .-`--`.                                              ')
    print('  | |        /Y . . Y\                             Press C to Play              ')
    print('  | |       // |   | \\                             Press Q to Quit              ')
    print('  | |      //  | . |  \\                            Press R to Credit            ')
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
        
        if input_key == 99:
            gotogame = True
            break
        
        if input_key == 113:
            gotogame = False
            break
        
        if input_key == 114:
            credit()
            
        if input_key == 48:
            gotogame = True
            cheat = True
            break
        
    if gotogame == True:
        main()
        
start()
