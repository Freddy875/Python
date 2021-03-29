MAX_ROWS = 49
MAX_COLS = 204

def createBoard(rows,cols):
    if type(rows) != int or type(cols) != int:
        return False
    
    if rows <= 1 or cols <= 1:
        return False

    if rows > MAX_ROWS or cols > MAX_COLS:
        return False

    #rows loop 
    for row in range(0, rows):
        # if the rows are even, print '|'
        if row % 2 == 0:
            for col in range(0, cols):
                # if the column is even, print spaces
                if col % 2 == 0:
                    endChar = ""
                    # if it is the last element, end with a new line
                    if col == cols - 1:
                        endChar = "\n"
                    print(" ", end = endChar)
                # if the columns are odd, print '|'
                else:
                    print("|", end="")

        # if the rows are odd, print '-'
        else:
            for col in range(0, col):
                endChar = ""
                # if it is the last element, end with a new line
                if col == cols - 1:
                    endChar = "\n"
                print("-", end=endChar)
    print("")
    return True

def BoardCreated(rows,cols):
    if(createBoard(rows,cols)):
        print("Here is your playing board.")
    else:
        print("Error. NO playing board for you.")

BoardCreated(3,3)

BoardCreated(5,5)



