import random


board = ["-", "-", "-"
         "-", "-", "-"
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print("---------------")
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print("---------------")
    print(board[6] + " | " + board[7] + " | " + board[8] )
    printBoard(board)

# take player input
def playerInput(board):
    inp = int(input("Enter a number between 0-8:"))
    if inp >= 0 and inp <= 8 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("OOPS ! Player is already there in that spot")

# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkRow(board): 
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] !="-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a TIE!")
        gameRunning = False

def checkWin():
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The WInner is {winner}")
    

# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"
# computer
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()

# check for Win or Tie
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)


