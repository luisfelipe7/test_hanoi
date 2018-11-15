# Author: Luis Felipe Castro Sánchez
# Creation Date: 15/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

# Execute Python : /usr/bin/python3
# Execute File: /usr/bin/python3  pathOfTheFile

from math import factorial
from sys import argv
import itertools
import functools


# *********************** Hanoi Solution by Felipe Castro  **************************

# Defining the sticks of the game

stick1 = []
stick2 = []
stick3 = []
numberOfMoves = 0
lastMoveValue = 0
numberOfStick = 0
numberOfElements = 0


# Defining a method to obtain next number of stick 


def obtainNumberOfNextStick():
    global numberOfStick
    if(numberOfStick == 1):
        return 2
    elif(numberOfStick == 2):
        return 3
    elif(numberOfStick == 3):
        return 1


# Defining a method to obtain the stick


def obtainStick():
    global stick1
    global stick2
    global stick3
    global numberOfStick
    if(numberOfStick == 1):
        return stick1
    elif(numberOfStick == 2):
        return stick2
    elif(numberOfStick == 3):
        return stick3


# Defining a method to obtain the next stick

def obtainStickNext(stickSucessionNumber):
    global stick1
    global stick2
    global stick3
    global numberOfStick
    if(numberOfStick == 1):
        if(stickSucessionNumber == 1):
            return stick2
        else:
            return stick3
    elif(numberOfStick == 2):
        if(stickSucessionNumber == 1):
            return stick3
        else:
            return stick1
    elif(numberOfStick == 3):
        if(stickSucessionNumber == 1):
            return stick1
        else:
            return stick2


# Make a move in the game


def makeMove(stickOne, sctickTwo):
    global lastMoveValue
    global numberOfElements
    global numberOfStick
    global numberOfMoves
    value = stickOne[len(stickOne)-1]
    if(value == lastMoveValue):
        if(numberOfStick == 1):
            numberOfStick = 2
        elif(numberOfStick == 2):
            numberOfStick = 3
        elif(numberOfStick == 3):
            numberOfStick = 1
    else:
        stickOne.pop()
        sctickTwo.append(value)
        lastMoveValue = value
        printingTheActualGame()
    makeMoves()


# Defining the method to make the moves


def makeMoves():
    global lastMoveValue
    global numberOfElements
    global numberOfStick
    global numberOfMoves
    if(theGameFinish(numberOfElements) is True):
        print("The game finish with "+str(numberOfMoves)+" moves, come back soon!")
    else:
        if(len(obtainStick()) != 0):
            if(len(obtainStickNext(1)) == 0):  # Make a move
                makeMove(obtainStick(), obtainStickNext(1))
            else:
                if((obtainStickNext(1)[len(obtainStickNext(1))-1]) < (obtainStick()[len(obtainStick())-1])):
                    if(len(obtainStickNext(2)) == 0):  # Make a move
                        makeMove(obtainStick(), obtainStickNext(2))
                    else:
                        if((obtainStickNext(2)[len(obtainStickNext(2))-1]) < (obtainStick()[len(obtainStick())-1])):
                            numberOfStick = obtainNumberOfNextStick()
                            makeMoves()
                        else:
                            makeMove(obtainStick(), obtainStickNext(2))
                else:
                    makeMove(obtainStick(), obtainStickNext(1))
        else:
            numberOfStick = obtainNumberOfNextStick()
            makeMoves()


# Defining the method to check if win


def theGameFinish(numberOfElements):
    global numberOfMoves
    winTheGame = True
    if(len(stick3) == numberOfElements):
        for i in range(0, numberOfElements):
            if(stick3[i] != numberOfElements-i):
                winTheGame = False
    else:
        winTheGame = False
    return winTheGame


# Printing the actual game


def printingTheActualGame():
    global numberOfMoves
    print()
    print("Making a Move:")
    print("Borigen) "+str(stick1))
    print("Bintermedia "+str(stick2))
    print("Bdestino "+str(stick3))
    numberOfMoves += 1
    input("Press a button to continue")


# Defining the method to start the game


def startGame():
    global lastMoveValue
    global numberOfElements
    global numberOfStick
    numberOfStick = 1
    lastMoveValue = -1
    print(" Starting the game, enter the number of discs for this game: ")
    numberOfElements = int(input())
    for i in range(0, numberOfElements):
        stick1.append(numberOfElements-i)
    print(" This is the initial game ")
    print("Borigen) "+str(stick1))
    print("Bintermedia "+str(stick2))
    print("Bdestino "+str(stick3))
    makeMoves()


startGame()
