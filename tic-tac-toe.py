#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Update the gameboard with the user input
def markBoard(position, mark):
    position = int(position)
    if board[position] == ' ':
        board[position] = mark

    
# Print the game board as described at the top of this code skeleton
def printBoard(board):
    copyBoard = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
    for i in copyBoard.keys():
        if board[i] == ' ':
            # change space to num
            copyBoard[i] = i
        else:
            copyBoard[i] = board[i]
    print( '\n' +
        str(copyBoard[1]) + " | " + str(copyBoard[2]) + " | " + str(copyBoard[3]) + '\n' +
        ' --------- \n' +
        str(copyBoard[4]) + " | " + str(copyBoard[5]) + " | " + str(copyBoard[6]) + '\n' +
        ' --------- \n' +
        str(copyBoard[7]) + " | " + str(copyBoard[8]) + " | " + str(copyBoard[9]) + '\n'
    )
    return 


# Check for wrong input, this function should return True or False.
def validateMove(position):
    position = int(position)
    if position >= 1 and position <= 9:
        if board[position] == ' ':
            return True

    return False


# List out all the combinations of winning, you will neeed this
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# Implement a logic to check if the previous winner just win
def checkWin(player):
    for win in winCombinations:
        if board[win[0]] == player and board[win[1]] == player and board[win[2]] == player:
            return True
    
    return False


# Implement a function to check if the game board is already full
def checkFull(board):
    for cell in board:
        if board[cell] == ' ':
            return False

    return True

def main():
    gameEnded = False
    currentTurnPlayer = 'X'
    # entry point of the whole program
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')
    # The game play logic
    # 1. Ask for user input and validate the input
    # 2. Update the board
    # 3. Check win or tie situation
    # 4. Switch User
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        if not move.isnumeric():
            print("Please Enter a Number 1-9!")
            continue
        if not validateMove(move):
            print("Invalid, please try again")
            continue
        markBoard(move,currentTurnPlayer)
        printBoard(board)
        if checkWin(currentTurnPlayer):
            print("Player " + currentTurnPlayer + " win the game")
            break
        if checkFull(board):
            print("Its a tie")
            break
        if currentTurnPlayer == 'X':
            currentTurnPlayer = 'O'
        else:
            currentTurnPlayer = 'X'
    # Implement the feature for the user to restart the game after a tie or game over        
    restart = input("Do you want to restart the game(y/n)?" ).lower()
    for i in board:
        if i <= 9 :
            board[i] = ' '
            continue
    if restart == 'y':
        main()
    else:
        exit()

main()
    
