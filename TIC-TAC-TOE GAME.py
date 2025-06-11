def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    #IN THE FIRST FOR IT CREATES ROW THEN IT IS AGAIN USED FOR THREE COLUMN
    current_player = 'X'

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("That cell is already occupied. Try again.")
            continue

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            display_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
