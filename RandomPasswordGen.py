# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:38:55 2021

@author: sophi
"""

# Random Password Generator

import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#array to represent menu
menu = ["[1] generate password", "[2] Exit Program"]

# initialize menu selection variable
menuSelect = "I can put anything in here"

# loop the whole program
while menuSelect != "2" :

    # for loop to print out menu options
    for i in menu:
        print(i)

    # Output to user select a menu option
    print("Select a menu option:\n")
    menuSelect = input()

    # conditional statements for selecting menu items
    if menuSelect == "1":
        uppercaseLetter1 = chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
        uppercaseLetter2 = chr(random.randint(65,90))
        lowercaseLetter1 = chr(random.randint(97,122))
        lowercaseLetter2 = chr(random.randint(97,122))
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        punctuationSign1 = chr(random.randint(33,38))
        punctuationSign2 = chr(random.randint(33,38))
        password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
        shuffle(password)
        print("Generated Password: " + password)
        print("Press Enter to Continue")
        input()
    elif menuSelect == "2":
        print("Goodbye")
    else: 
        print("invalid key, press enter to continue...")
        input()


    # clear
    print("\n\n\n\n\n\n\n\n\n")
