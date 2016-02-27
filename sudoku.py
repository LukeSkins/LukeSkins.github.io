from random import randint

def print_board(board):
    rowCounter = 0
    for row in board:
        rowStr = ""
        sectionCounter = 0
        rowEndCounter = 0
        for cell in row:
            rowStr = rowStr + str(cell) + " "
            sectionCounter = sectionCounter + 1
            if sectionCounter == 3 and rowEndCounter <= 1:
                rowStr = rowStr  + "| "
                sectionCounter = 0
                rowEndCounter = rowEndCounter + 1
        print rowStr
        rowCounter = rowCounter + 1
        if rowCounter == 3 or  rowCounter == 6:
            print "- - - - - - - - - - -"

def checkNumber(a, b):
    num = board[a][b]
    for x in range(9):
        if board[a][x] == num and x != b:

            print str(num) +" " + str(board[a][x]) + "True"
            return True
        else:
            #print str(num) +" " + str(board[a][x]) + "False"
            return False


board = []
for i in range(9):
    row = []
    for x in range(9):
        row.append(randint(1,9))
    board.append(row)

rowCount = 0
totalloops = 0
while rowCount < 9:
    cellCount = 0
    while cellCount < 9:
        if checkNumber(rowCount, cellCount):
            board[rowCount][cellCount] = randint(1,9)
        else:
            cellCount = cellCount + 1
        totalloops = totalloops + 1
        if totalloops > 9999999:
            break
    rowCount = rowCount + 1


print print_board(board)
