# This is my first personal project I will make in python
# Hangman Game
import random
words = ["academy", "department", "faculty", "hall", "institute", "institution", "seminary", "university"]
randomWord = random.choice(words)
lettersGuessed = ""

turnCount = int(input("How many guesses would you like to start with? "))

while turnCount > 0:
    guess = input("Enter a letter: ")

    if guess in randomWord:
        print(f"Correct! There is one or more {guess} in the secret word. {turnCount} turn(s) left")
    else:
        turnCount -= 1
        print(f"Incorrect! There is no {guess} in the secret word. {turnCount} turn(s) left")

    lettersGuessed += guess
    wrongLetter = 0

    for letter in randomWord:
        if letter in lettersGuessed:
            print(f"{letter}", end = "")
        else:
            print("_", end = "")
            wrongLetter += 1
    print("")

    if wrongLetter == 0:
        print(f"Congratulations! The secret word was: {randomWord}. You won!")
        break
else:
    print(f"Sorry! The secret word was: {randomWord}. You lost")