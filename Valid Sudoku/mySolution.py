def isValidSudoku(self, board):
    elementTracker = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            curPos = board[i][j]
            if curPos != ".":
                rowIndex = "Row:" + str(i) + "num:" + str(curPos)
                colIndex = "Col:" + str(j) + "num:" + str(curPos)
                boxIndex = "boxRow:" + \
                    str(i//3) + "boxCol:" + str(j//3) + "num:" + str(curPos)
                if rowIndex in elementTracker or colIndex in elementTracker or boxIndex in elementTracker:
                    elementTracker.clear()
                    return False
                else:
                    elementTracker.add(rowIndex)
                    elementTracker.add(colIndex)
                    elementTracker.add(boxIndex)
    elementTracker.clear()
    return True
