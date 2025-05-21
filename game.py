import sys
import os
import time
from grid import Grid

os.system("clear")
if len(sys.argv) > 1:
    # sys.argv[1] is the first argument after the script name
    argument = int(sys.argv[1])
else:
    print("No argument provided.")
    exit()
guesses = 0
manualReveals = 0
giveUpFlag = False
grid = Grid(argument)
while True:
    os.system("clear")
    grid.printGrid()
    totalReveals = 0
    gameOver = False
    for key, value in grid.elements.items():
        if giveUpFlag:
            print("\nYou have given up, Game Over!")
            gameOver = True
            break
        if manualReveals == grid.numOfElements:
            print("\nYou cheated - Loser! Your score is 0.0!")
            gameOver = True
            break
        if value[1]:
            totalReveals += 1
        if totalReveals == grid.numOfElements:
            gameOver = True
            grid.calcScore(guesses)
            print("\nYou won! Your score is: " + str(format(grid.score, ".2f")))
    print("\n1. Let me select two elements\n2. Uncover one element for me\n3. I give up - reveal the grid\n4. New game\n5. Exit\n")
    while True:
        try:
            choice = int(input("Select: "))
            if choice > 5 or choice < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, try again.")
    if gameOver and (choice == 1 or choice == 2 or choice == 3):
        print("Game is over, choose a different option.")
        time.sleep(3)
        continue
    if choice == 1:
        while True:
            elementChoice1 = input("Enter element #1 coordinates (e.g., A0):  ")
            if elementChoice1:
                elementChoice1 = elementChoice1.upper().strip()
            if not elementChoice1:
                elementChoice1 = " "
            if elementChoice1 not in grid.elements.keys() and elementChoice1[0] not in grid.columns:
                print("Column entry is out of range for element #1, try again.")
                continue
            elif elementChoice1 not in grid.elements.keys() and elementChoice1[1] not in grid.rows:
                print("Row entry is out of range for element #1, try again.")
                continue
            break
        while True:
            elementChoice2 = input("Enter element #2 coordinates (DIFFERENT from element #1):  ")
            if elementChoice2:
                elementChoice2 = elementChoice2.upper().strip()
            if not elementChoice2:
                elementChoice2 = " "
            if elementChoice2 not in grid.elements.keys() and elementChoice2[0] not in grid.columns:
                print("Column entry is out of range for element #2, try again.")
                continue
            elif elementChoice2 not in grid.elements.keys() and elementChoice2[1] not in grid.rows:
                print("Row entry is out of range for element #2, try again.")
                continue
            elif elementChoice1 == elementChoice2:
                print("element #2 can't be the same as element #1, try again.")
                continue
            break
        if grid.elements[elementChoice1][1] and grid.elements[elementChoice2][1]:
            print("Both elements are already revealed.")
            time.sleep(3)
        if grid.elements[elementChoice1][1]:
            count = 0
            for key, value in grid.elements.items():
                if value[0] == grid.elements[elementChoice1][0] and value[1] and grid.elements[elementChoice1][1]:
                    count += 1
            if count == 2:
                print("The pair of " + elementChoice1 + " has been revealed already.")
                time.sleep(3)
                continue
        if grid.elements[elementChoice2][1]:
            count = 0
            for key, value in grid.elements.items():
                if value[0] == grid.elements[elementChoice2][0] and value[1] and grid.elements[elementChoice2][1]:
                    count += 1
            if count == 2:
                print("The pair of " + elementChoice2 + " has been revealed already.")
                time.sleep(3)
                continue
        else:
            guesses += 1
            elementFlag1 = False
            elementFlag2 = False
            if grid.elements[elementChoice1][1]:
                elementFlag1 = True
            if grid.elements[elementChoice2][1]:
                elementFlag2 = True
            grid.elements[elementChoice1][1] = True
            grid.elements[elementChoice2][1] = True
            if grid.elements[elementChoice1][0] != grid.elements[elementChoice2][0]:
                os.system("clear")
                grid.printGrid()
                time.sleep(2)
                if not elementFlag1:
                    grid.elements[elementChoice1][1] = False
                if not elementFlag2:
                    grid.elements[elementChoice2][1] = False
    if choice == 2:
        while True:
            elementChoice1 = input("Enter element coordinates (e.g., A0):  ")
            if elementChoice1:
                elementChoice1 = elementChoice1.upper().strip()
            if not elementChoice1:
                elementChoice1 = " "
            if elementChoice1 not in grid.elements.keys() and elementChoice1[0] not in grid.columns:
                print("Column entry is out of range for the element, try again.")
                continue
            elif elementChoice1 not in grid.elements.keys() and elementChoice1[1] not in grid.rows:
                print("Row entry is out of range for the element, try again.")
                continue
            break
        if grid.elements[elementChoice1][1]:
            print("Element " + elementChoice1 + " is already revealed.")
            time.sleep(3)
        else:
            grid.elements[elementChoice1][1] = True
            guesses += 2
            manualReveals += 1
    if choice == 3:
        for key, value in grid.elements.items():
            value[1] = True
        giveUpFlag = True
    if choice == 4:
        grid = Grid(argument)
        giveUpFlag = False
        guesses = 0
        manualReveals = 0
    if choice == 5:
        print("Thanks for playing Brain Buster!")
        break

