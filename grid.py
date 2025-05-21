import random


class Grid:
    def __init__(self, size):
        if (size != 2) and (size != 4) and (size != 6):
            print("Invalid size, program won't run.")
            exit()
        self.numOfElements = size * size
        self.columns = list(range(65, 65 + size))
        for i in range(size):
            self.columns[i] = chr(self.columns[i])
        self.rows = list(range(0, 0 + size))
        self.elements = {}
        elementValues = []
        for i in range(int(self.numOfElements / 2)):
            elementValues += [i, i]
        for i in range(size):
            for x in range(size):
                self.elements[self.columns[i] + str(self.rows[x])] = [elementValues.pop(
                    random.randint(0, len(elementValues)-1)), False]

    def calcScore(self, guesses):
        self.score = (int(self.numOfElements / 2)/guesses) * 100

    def printGrid(self):
        print("-"*20 + "\n|   Brain Buster   |\n" + "-"*20 + "\n")
        columnString = "    "
        for i in self.columns:
            columnString += "\t[" + i + "]\t"
        rowString = ""
        for i in range(len(self.rows)):
            rowString += "\n[" + str(i) + "]\t "
            for key in self.elements:
                if str(i) in key:
                    if self.elements[key][1]:
                        rowString += str(self.elements[key][0]) + "\t\t "
                    else:
                        rowString += "X\t\t "
        print(columnString + rowString)
