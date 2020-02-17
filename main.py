"""
Author: John Kear
Version: v1.0
Date: 2/17/2020

Comments:
This program will allow the user to convert an english sentence into Morse code or vice versa
When converting Morse code to english, the user must put a space between letters, and two spaces between words.

"""


def morse_to_english(message):
    print("Morse to English")

def english_to_morse(message):
    print("English to Morse")

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6',
         '7', '8', '9', '.', ' '
]

morse = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
    "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
    "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
    "-.--", "--..", "-----", ".----", "..---", "...--", "....-",
    ".....", "-....", "--...", "---..", "----.", ".-.-.-", "......."
]

userInput = [""]
userCont = True
userOption = 0
isValid = False

print("This program converts a message from English to Morse code or vice versa.\n"
      "When converting a message from Morse code to English, a space must be placed between each letter\nand two spaces"
      " must be used to indicate a space between words.")

while userCont:
    userOption = input("If you would like to convert a message from English to Morse code enter 0\n"
                       "If you would like to convert a message from Morse code to English enter 1\n"
                       "If you would like to quit enter 2: ")
    while not isValid:
        try:
            userOption = int(userOption)
            if userOption == 0 or userOption == 1 or userOption == 2:
                print("You entered:", userOption)
                isValid = True
            else:
                print("You entered an invalid option.")
                userOption = input("To convert from English to Morse code enter 0\n"
                                   "To convert from Morse code to English enter 1\n"
                                   "To quite enter 2: ")
        except ValueError:
            print("You entered an invalid option.")
            userOption = input("To convert from English to Morse code enter 0\n"
                               "To convert from Morse code to English enter 1\n"
                               "To quite enter 2: ")

    if userOption == 0:
        print("You have opted to convert from English to Morse code.")
        userInput = input("Please enter a message to be converted:\n")
        english_to_morse(userInput)
    elif userOption == 1:
        print("You have opted to convert from Morse code to English.")
        userInput = input("Please enter a message to be converted:\n")
        morse_to_english(userInput)
    elif userOption == 2:
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
