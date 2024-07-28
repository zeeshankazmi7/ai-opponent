# name: zeeshan kazmi
# last change: 27/03/24

from tabulate import tabulate
import math

def createBoard():
    # initialize a 3x3 grid with empty spaces
    grid = [[" " for _ in range(3)] for _ in range(3)]
    # format and display the grid as a table
    board = tabulate(grid, tablefmt="grid")
    print(board)
    return grid

def playerTurn(grid):
    while True:
        try:
            # prompt the player to choose a square (1-9)
            turnSquare = int(input("Enter which square you would like to take (1-9): "))
            # calculate the corresponding row and column
            row = (turnSquare - 1) // 3
            col = (turnSquare - 1) % 3
            # check if the chosen square is valid and empty
            if 1 <= turnSquare <= 9 and grid[row][col] == " ":
                # place the player's marker on the grid
                grid[row][col] = "X"
                break
            else:
                print("Invalid input. Please enter a valid empty square (1-9).")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # update and display the board
    board = tabulate(grid, tablefmt="grid")
    print(board)
    return grid

def aiTurn(grid):
    # initialize best score and move for ai
    bestScore = -math.inf
    bestMove = None

    # iterate over all grid cells to find the best move
    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                # simulate ai's move
                grid[row][col] = "O"
                # evaluate the move using minimax
                score = minimax(grid, False)
                # undo the move
                grid[row][col] = " "
                # update best move if this one is better
                if score > bestScore:
                    bestScore = score
                    bestMove = (row, col)

    # make the best move found
    grid[bestMove[0]][bestMove[1]] = "O"
    print("\nai chooses square:", bestMove[0] * 3 + bestMove[1] + 1)
    # update and display the board
    board = tabulate(grid, tablefmt="grid")
    print(board)
    return grid

def minimax(grid, isMax):
    # check if the game is won or drawn
    if checkWinner(grid, "X"):
        return -1
    elif checkWinner(grid, "O"):
        return 1
    elif not any(" " in row for row in grid):
        return 0

    # maximize ai's score
    if isMax:
        bestScore = -math.inf
        for row in range(3):
            for col in range(3):
                if grid[row][col] == " ":
                    grid[row][col] = "O"
                    score = minimax(grid, False)
                    grid[row][col] = " "
                    bestScore = max(score, bestScore)
        return bestScore
    # minimize player's score
    else:
        bestScore = math.inf
        for row in range(3):
            for col in range(3):
                if grid[row][col] == " ":
                    grid[row][col] = "X"
                    score = minimax(grid, True)
                    grid[row][col] = " "
                    bestScore = min(score, bestScore)
        return bestScore

def checkWinner(grid, player):
    # check for a win in any row
    for row in grid:
        if row.count(player) == 3:
            return True

    # check for a win in any column
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] == player:
            return True

    # check for a win in both diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True

    return False

def main():
    print("welcome to the cancer treatment decision simulator.\n")
    print("this is a game of tic tac toe where you as the doctor decide on treatment decisions that the cancer will respond to.\n")
    print("the game board represents the current patient profile, which you and the cancer take turns in altering.\n")
    # create the initial game board
    grid = createBoard()

    while True:
        # player's turn
        grid = playerTurn(grid)
        # check if player wins or the game is a draw
        if checkWinner(grid, "X"):
            print("treatment succesful!")
            break
        if not any(" " in row for row in grid):
            print("draw.")
            break

        # ai's turn
        grid = aiTurn(grid)
        # check if ai wins or the game is a draw
        if checkWinner(grid, "O"):
            print("treatment failed!")
            break
        if not any(" " in row for row in grid):
            print("draw.")
            break

main()
