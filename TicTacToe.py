#
# Christopher Coronado
# CSC 120
# 12/12/2021
# The purpose of this program is to create a Tic Tac Toe game playable by two people

board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in board:
    board_keys.append(key)


def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(board)
        print("It's your turn," + turn + ". Move to which place?")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # For every move after 5 moves check which player won.
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':  # Across the top
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':  # Across the middle
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['1'] == board['2'] == board['3'] != ' ':  # Across the bottom
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':  # Down the left side
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':  # Down the middle
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':  # Down the right side
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['7'] == board['5'] == board['3'] != ' ':  # Diagonal
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':  # Diagonal
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        # Call a tie.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Alternate players.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Play again?
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key] = " "

        game()


if __name__ == "__main__":
    game()
