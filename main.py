"""
Author: John Kear
Version: v1.0
Date: 2/17/2020

Comments:
This program will allow the user to convert an english sentence into Morse code or vice versa
When converting Morse code to english, the user must put a space between letters, and two spaces between words.

"""
import constant


def morse_to_english(message):
    print("Morse to English")
    # iterate through message until space is found, adding symbols to temp variable
    # when space is found, check for double space, if double space add space to converted message
    # if only single space is found, iterate through morse list until match is found
    # add corresponding alpha (using index number) to the converted message
    # return converted message to main program


def english_to_morse(message):
    print("English to Morse")
    # iterate through message setting current character to temp variable
    # compare current character to alpha list
    # add corresponding Morse code sequence to converted message
    # add space to converted message after every sequence
    # if a space is encountered in original message, add two spaces to converted message
    # return converted message to main program


userInput = [""]
userCont = True
userOption = 0
isValid = False

print("This program converts a message from English to Morse code or vice versa.\n"
      "When converting a message from Morse code to English, a space must be placed between each letter\nand two spaces"
      " must be used to indicate a space between words.")

while userCont:
    userOption = input("Please enter an option:\n"
                       "1. English to Morse code\n"
                       "2. Morse code to English\n"
                       "3. Quit:\n")
    while not isValid:
        try:
            userOption = int(userOption)
            if userOption == 1 or userOption == 2 or userOption == 3:
                print("You entered:", userOption)
                isValid = True
            else:
                print("You entered an invalid option.")
                userOption = input("To convert from English to Morse code enter 1\n"
                                   "To convert from Morse code to English enter 2\n"
                                   "To quite enter 3:\n")
        except ValueError:
            print("You entered an invalid option.")
            userOption = input("To convert from English to Morse code enter 1\n"
                               "To convert from Morse code to English enter 2\n"
                               "To quite enter 3:\n")

    if userOption == 1:
        print("You have opted to convert from English to Morse code.")
        userInput = input("Please enter a message to be converted:\n")
        english_to_morse(userInput)
    elif userOption == 2:
        print("You have opted to convert from Morse code to English.")
        userInput = input("Please enter a message to be converted:\n")
        morse_to_english(userInput)
    elif userOption == 3:
        print("Goodbye.")
        exit(0)

    userOption = input("Would you like to convert another message? y for yes or n for no: ")
    isValid = False

    while not isValid:
        if userOption == 'y':
            userCont = True
            isValid = True
        elif userOption == 'n':
            print("Goodbye")
            userCont = False
            isValid = True
        else:
            userOption = input("You have entered an invalid value. Enter y to continue or n to quit: ")

    isValid = False
