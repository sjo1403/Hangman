"""
This py_project is the game Hangman

3. If the game is lost or won, the user can play the game again by typing "play" when prompted

4. The user can quit the game at any time by typing "quit"

5. Exception handling:
    -Numbers, special characters, and spaces will throw an exception and prompt the user to enter a valid character (alpha) or quit
    -Strings other than "quit" will throw an exception and prompt the user to enter a valid character or quit

6. Extras:
    -Users can select a difficulty level
    -Total wins and losses will be tallied for each session of Hangman
"""

# 1. The computer selects a Secret Word from a predefined list

from random import randint
from random import seed

seed(a=None)
random_int = randint(0, 6)

sWords = ["butterfly", "pineapple", "history", "fortune", "cinema", "artist", "symbolism"]
secretWordString = sWords[random_int]

secretWord = []
i = 0
for char in secretWordString:
    secretWord.append(secretWordString[i])
    i += 1

difficulty = {"easy": 10, "normal": 7, "hard": 4}

print("Welcome to Hangman!\n\nSelect a difficulty level:")
settingStrings = input("Type 'EASY', 'NORMAL', or 'HARD'")
setting = settingStrings.lower()

IGC = difficulty[setting]

print("You've selected " + setting + " mode.")
print("\nFigure out the Secret Word in less than " + str(IGC) + " incorrect guesses, or it's game over!")

"""
2. The user guesses a letter for the Secret Word
    a) If the letter is found in the Secret Word:
        -the letter is added to the position of the Secret Word;
            ie if the "x" is guessed correctly, "_____" becomes "___x_"
        -the user's Incorrect Guess Count (IGC) does not change
    b) If the letter is not found in the Secret Word:
        -the letter is added to a bank of incorrect letters so the user does not input the same incorrect letter
            if a duplicate letter is input, this will not count against their IGC
        -the user's IGC decreases by 1
    c) If all letters in the Secret Word are guessed before the IGC reaches 0, the user wins the game
    d) If the IGC reaches 0, the user loses the game
"""
guesses = IGC

print(secretWord)

word = []
wrongLetters = []

i = 0
for char in secretWord:
    word.append("-")
    i += 1

while guesses > 0 and word != secretWord:
    print("\nGuess a letter:")
    letter = input()

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
    print("\n\nGame over! The Secret Word was: " + secretWordString)

else:
    print("\n\nYou win! The secret Word is: " + secretWordString)
