"""

This py_project is the game Hangman

"""

"""

5. Exception handling:

    -Numbers, special characters, and spaces will throw an exception and prompt the user to enter a valid character (alpha) or quit

    -Strings other than "quit" will throw an exception and prompt the user to enter a valid character or quit

6. Extras:


    -Total wins and losses will be tallied for each session of Hangman

"""

import sys

losses = 0
wins = 0

#game is set to autoloop unless player enters "quit"
while True:

    from random import randint
    from random import seed

    seed(a=None)
    random_int = randint(0, 6)

    sWords = ["butterfly", "pineapple", "history", "fortune", "cinema", "artist", "symbolism"]
    secretWordString = sWords[random_int]

    #secretWord is an array of characters so that the letters in the Secret Word can be compared to guess letters
    secretWord = []     
    i = 0
    for char in secretWordString:
        secretWord.append(secretWordString[i])
        i += 1

    #key-value pair used for difficulty setting
    #dictionary value is the Incorrect Guess Count (IGC)
    difficulty = {"easy": 10, "normal": 7, "hard": 4}
    print("\n\nWelcome to Hangman!\n\nSelect a difficulty level:")

    while True:
        settingStrings = input("Type 'EASY', 'NORMAL', or 'HARD', or type 'QUIT' to exit the game.")
        setting = settingStrings.lower()

        if (setting == "easy" or setting == "normal" or setting == "hard"):
            break

        elif setting == "quit":
            print("Thanks for playing!")
            sys.exit() 

        else:
            print("\nInvalid entry.")

    #Incorrect Guess Count
    IGC = difficulty[setting]
    print("You've selected " + setting + " mode.")

    print("\nFigure out the Secret Word in less than " + str(IGC) + " incorrect guesses, or it's game over!")

    guesses = IGC

    #word shows the correctly guessed letters of the Secret Word, while wrongLetters shows the incorrectly guessed letters
    word = []
    wrongLetters = []
    i = 0
    for char in secretWord:
        word.append("-")
        i += 1

    while guesses > 0 and word != secretWord:
        print("\n\nGuess a letter:")
        letter = input()

        #if player enters "quit", the game exits
        if letter.lower() == "quit":
            print("Thanks for playing!")
            sys.exit() 

        #the following two if statements catch unoriginal letter entries
        if letter in wrongLetters:
            print("The letter " + letter + " has already been guessed incorrectly.")
            continue

        if letter in word:
            print("The letter " + letter + " has already been guessed correctly.")
            continue

        #nullCount increases if letter is not found in Secret Word
        #if nullCount is equal to the length of the Secret Word, the letter is not in the Secret Word
        nullCount = 0
        i = 0

        for char in secretWord:

            if letter != secretWord[i]:
                nullCount += 1

                if nullCount == len(secretWord):
                    print("The letter " + letter + " is not in the Secret Word.")
                    print("You lose 1 guess.")
                    wrongLetters.append(letter)
                    guesses -= 1

            else:
                word[i] = letter

            i += 1

        print("Correct letters:")

        for char in word:
            print(char, end=" ")

        print("\n\nIncorrect letters:")

        for char in wrongLetters:
            print(char, end=" ")

        print("Incorrect guesses left: " + str(guesses))

    if guesses == 0:
        losses += 1
        print("\n\nGame over! The Secret Word was: " + secretWordString)

    else:
        wins += 1
        print("\n\nYou win! The Secret Word is: " + secretWordString)

    if wins > 0:
        print("Wins: " + str(wins))

    if losses > 0:
        print("Losses: " + str(losses))
