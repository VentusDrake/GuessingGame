import random
import math


# Variables
counterAI = 0
counterPlayer = 0
gameLoop = True
askStart = True

# Functions
def algorithmEasy():
    numToGuess = random.randint(1, 100)
    topNumber = 100
    guess = 50
    counterAI = 0
    # Guessing algorythm
    AIGuessed = False
    while AIGuessed == False:

        if guess == numToGuess:
            AIGuessed = True
        elif numToGuess < guess:
            tmp = guess  # Algorithm takes guesses by dividing the difference
            guess -= math.ceil((topNumber - guess) / 2)  # Between previous the biggest number and guess in a half
            topNumber = tmp
        elif numToGuess > guess:
            guess += math.ceil((topNumber - guess) / 2)

        counterAI += 1

    print("AI guessed the number with " + str(counterAI) + " moves")
    return counterAI


def algorithmMedium():
    numToGuess = random.randint(1, 1000)
    topNumber = 1000
    guess = 500
    counterAI = 0
    # Guessing algorythm
    AIGuessed = False
    while AIGuessed == False:

        if guess == numToGuess:
            AIGuessed = True
        elif numToGuess < guess:
            tmp = guess  # Algorithm takes guesses by dividing the difference
            guess -= math.ceil((topNumber - guess) / 2)  # Between previous the biggest number and guess in a half
            topNumber = tmp
        elif numToGuess > guess:
            guess += math.ceil((topNumber - guess) / 2)

        counterAI += 1

    print("AI guessed the number with " + str(counterAI) + " moves")
    return counterAI


def algorithmHard():
    numToGuess = random.randint(1, 10000)
    topNumber = 10000
    guess = 5000
    counterAI = 0
    # Guessing algorythm
    AIGuessed = False
    while AIGuessed == False:

        if guess == numToGuess:
            AIGuessed = True
        elif numToGuess < guess:
            tmp = guess  # Algorithm takes guesses by dividing the difference
            guess -= math.ceil((topNumber - guess) / 2)  # Between previous the biggest number and guess in a half
            topNumber = tmp
        elif numToGuess > guess:
            guess += math.ceil((topNumber - guess) / 2)

        counterAI += 1

    print("AI guessed the number with " + str(counterAI) + " moves")
    return counterAI


def playerGuessEasy():

    # Player guessing
    print("Now it's your turn! Do your best!")
    print("Guess the number between 1 and 100 - Good Luck!")
    numToGuess = random.randint(1, 100)
    playerGuessed = False
    counterPlayer = 0
    while playerGuessed == False:
        try:
            pGuess = int(input("Guess the number: "))
            if pGuess <= 0 or pGuess > 100:
                print("Choose number between 1 and 100")
            else:
                if pGuess == numToGuess:
                    playerGuessed = True
                elif pGuess > numToGuess:
                    print("Lower!")
                elif pGuess < numToGuess:
                    print("Higher")
                counterPlayer += 1
        except:
            print("Wrong input!")
    return counterPlayer


def playerGuessMedium():
    # Player guessing
    print("Now it's your turn! Do your best!")
    print("Guess the number between 1 and 1000 - Good Luck!")
    numToGuess = random.randint(1, 1000)
    playerGuessed = False
    counterPlayer = 0
    while playerGuessed == False:
        try:
            pGuess = int(input("Guess the number: "))
            if pGuess <= 0 or pGuess > 1000:
                print("Choose number between 1 and 1000")
            else:
                if pGuess == numToGuess:
                    playerGuessed = True
                elif pGuess > numToGuess:
                    print("Lower!")
                elif pGuess < numToGuess:
                    print("Higher")
                counterPlayer += 1
        except:
            print("Wrong input!")
    return counterPlayer


def playerGuessHard():
    # Player guessing
    print("Now it's your turn! Do your best!")
    print("Guess the number between 1 and 10000 - Good Luck!")
    numToGuess = random.randint(1, 10000)
    playerGuessed = False
    counterPlayer = 0
    while playerGuessed == False:
        try:
            pGuess = int(input("Guess the number: "))
            if pGuess <= 0 or pGuess > 100:
                print("Choose number between 1 and 100")
            else:
                if pGuess == numToGuess:
                    playerGuessed = True
                elif pGuess > numToGuess:
                    print("Lower!")
                elif pGuess < numToGuess:
                    print("Higher")
                counterPlayer += 1
        except:
            print("Wrong input!")
    return counterPlayer


def introduction():
    print("Welcome to the Guessing Game!")
    print("Today you will fight against the smartest algorithm in the world!!")


# Main Loop
while gameLoop:

    try:
        if(askStart):
            choice = str(input("Do you want to play Guessing Game? (y/n): "))
            # Choice isn't case sensitive

        if choice.lower() == "y":

            # Introduction
            if(askStart):
                introduction()

            # Choosing Level
            choosingLevel = True
            while choosingLevel:
                try:
                    print("Difficulty:")
                    print("Easy (1-100)")
                    print("Medium (1-1000)")
                    print("Hard (1-10000)")
                    selectLevel = str(input("What difficulty you want to play?: "))
                    choosingLevel = False
                except:
                    print("Wrong type of input! Expected String")
                    choosingLevel = True

                if selectLevel.lower() == "easy":

                    # Assigning to counterAI number of moves which algorithm made
                    counterAI = algorithmEasy()

                    # Assigning to counterPlayer number of moves which player made
                    counterPlayer = playerGuessEasy()

                    # Checking if player won with AI
                    if counterPlayer < counterAI:
                         print("Wow!! you got it and also you are better than the smartest AI!! CONGRATULATIONS!")
                    else:
                         print("Well you did it with " + str(counterPlayer) + " congratulations! But unluckily you didn't beat the AI")

                    askStart = True

                elif selectLevel.lower() == "medium":

                    counterAI = algorithmMedium()

                    counterPlayer = playerGuessMedium()

                    if counterPlayer < counterAI:
                         print("Wow!! you got it and also you are better than the smartest AI!! CONGRATULATIONS!")
                    else:
                         print("Well you did it with " + str(counterPlayer) + " congratulations! But unluckily you didn't beat the AI")

                    askStart = True

                elif selectLevel.lower() == "hard":

                    counterAI = algorithmHard()

                    counterPlayer = algorithmHard()

                    if counterPlayer < counterAI:
                        print("Wow!! you got it and also you are better than the smartest AI!! CONGRATULATIONS!")
                    else:
                        print("Well you did it with " + str(counterPlayer) + " congratulations! But unluckily you didn't beat the AI")

                    askStart = True

                # Difficulty doesn't exist
                else:
                    print("Type correct level!")
                    askStart = False

        # Quitting
        elif choice.lower() == "n":
            print("See you soon!")
            gameLoop = False
        else:
            print("Wrong input!")
    except:
        print("Wrong type of input!")
