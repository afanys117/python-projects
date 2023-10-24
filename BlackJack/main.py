import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

usersCards = []
computersCards = []
usersScore = 0
computersScore = 0
# userWin = False
# computerWin = False


def getCard(list):
    list.append(random.choice(cards))


def updateUserScore():
    global usersScore
    usersScore = 0
    for item in usersCards:
        usersScore += item


def updateComputerScore():
    global computersScore
    computersScore = 0
    for item in computersCards:
        computersScore += item


def checkUserBlackJack():
    # global usersScore
    if (11 in usersCards) and (10 in usersCards) and (usersScore == 21):
        # global userWin
        userWin = True
    else:
        userWin = False
    return userWin


def checkComputerBlackJack():
    # global computersScore
    if (11 in computersCards) and (10 in computersCards) and (computersScore == 21):
        # global computerWin
        computerWin = True
    else:
        computerWin = False
    return computerWin


def checkUserScore():
    booleanCheck = False
    global usersCards
    if (usersScore > 21) and (11 not in usersCards):
        booleanCheck = False
    elif (usersScore > 21) and (11 in usersCards):
        usersCards[usersCards.index(11)] = 1
        updateUserScore()
        checkUserScore()
    elif usersScore <= 21:
        booleanCheck = True
    return booleanCheck


def printDetails():
    print(f"The user's cards are {usersCards}")
    print(f"The computer's cards are {computersCards}")
    print(f"Users score is {usersScore}")
    print(f"Computers score is {computersScore}")


def checkComputerScore():
    booleanCheck = False
    global computersCards
    if (computersScore > 21) and (11 not in computersCards):
        booleanCheck = False
    elif (computersScore > 21) and (11 in computersCards):
        computersCards[computersCards.index(11)] = 1
        updateComputerScore()
        checkComputerScore()
    elif computersScore <= 21:
        booleanCheck = True
    return booleanCheck


endOfProgram = False

while not endOfProgram:
    print(art.logo)
    for number in range(2):
        getCard(usersCards)
        getCard(computersCards)
    updateUserScore()
    updateComputerScore()
    printDetails()
    if checkUserBlackJack() and checkComputerBlackJack():
        printDetails()
        print("Draw")
        endOfProgram = True
    elif checkUserBlackJack() or checkComputerBlackJack():
        if checkUserBlackJack():
            printDetails()
            print("You won")
        else:
            printDetails()
            print("You lose")
        endOfProgram = True
    elif not checkUserScore():
        printDetails()
        print("You lose")
        endOfProgram = True
    elif checkUserScore():
        endOfLoop = False
        while not endOfLoop:
            if input("Do you want to draw another card, 'y' or 'n'\n") == 'y':
                getCard(usersCards)
                updateUserScore()
                if checkUserBlackJack():
                    print("You win")
                    endOfProgram = True
                    endOfLoop = True
                elif not checkUserScore():
                    print("You lose")
                    endOfProgram = True
                    endOfLoop = True
                printDetails()
            else:
                endOfLoop = True
        # while (input("Do you want to draw another card, 'y' or 'n'\n") == 'y') and not endOfProgram:
        #     getCard(usersCards)
        #     updateUserScore()
        #     if checkUserBlackJack():
        #         print("You win")
        #         endOfProgram = True
        #     elif not checkUserScore():
        #         print("You lose")
        #         endOfProgram = True
        #     printDetails()

    if not endOfProgram:
        while computersScore <= 16:
            getCard(computersCards)
            updateComputerScore()
        if not checkComputerScore():
            printDetails()
            print("You won")
            endOfProgram = True

    if not endOfProgram:
        if usersScore == computersScore:
            printDetails()
            print("Draw")
            endOfProgram = True
        elif usersScore > computersScore:
            printDetails()
            print("You won")
            endOfProgram = True
        elif computersScore > usersScore:
            printDetails()
            print("You lose")
            endOfProgram = True
    endOfProgram = True
