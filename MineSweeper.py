
import random

def initialize_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mine_locations = random.sample(range(rows * cols), mines)

    for mine_location in mine_locations:
        row = mine_location // cols
        col = mine_location % cols
        board[row][col] = '*'

    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
            if board[i][j] == '*':
                count += 1
    return count

def reveal_empty_cells(board, row, col, visited):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col]:
        return

    visited[row][col] = True

    if board[row][col] == ' ':
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
                reveal_empty_cells(board, i, j, visited)

def play_game(rows, cols, mines):
    board = initialize_board(rows, cols, mines)
    revealed_cells = [['False' for _ in range(cols)] for _ in range(rows)]

    while True:
        print_board(revealed_cells)
        row = int(input("Enter row (0 to {}): ".format(rows - 1)))
        col = int(input("Enter column (0 to {}): ".format(cols - 1)))

        if board[row][col] == '*':
            print("Game Over! You hit a mine.")
            print_board(board)
            break
        else:
            adjacent_mines = count_adjacent_mines(board, row, col)
            revealed_cells[row][col] = str(adjacent_mines)
            
            if adjacent_mines == 0:
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                reveal_empty_cells(board, row, col, visited)

            if all(cell != ' ' for row in revealed_cells for cell in row):
                print("Congratulations! You won!")
                print_board(board)
                break

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    mines = int(input("Enter the number of mines: "))

    play_game(rows, cols, mines)

