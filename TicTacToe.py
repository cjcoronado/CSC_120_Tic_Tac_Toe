#
# Christopher Coronado
# CSC 120
# 12/12/2021
# The purpose of this program is to create a two player Tic Tac Toe game.

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
        print(f"It's your turn, {turn}. Place your mark.")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nPlace your mark in a different spot.")
            continue

        # For every move after 5 moves check which player won.
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':  # Top row win
                print_board(board)
                print("\nGame Over.\n")
                print(f"{turn} is the winner! Bow down to {turn}'s superior TicTacToe skills!")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':  # Middle row win
                print_board(board)
                print("\nGame Over.\n")
                print(f"{turn} is the winner! Bow down to {turn}'s superior TicTacToe skills!")
                break
            elif board['1'] == board['2'] == board['3'] != ' ':  # Bottom row win
                print_board(board)
                print("\nGame Over.\n")
                print(f"{turn} is the winner! Bow down to {turn}'s superior TicTacToe skills!")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':  # Left column win
                print_board(board)
                print("\nGame Over.\n")
                print(f"{turn} is the winner! Bow down to {turn}'s superior TicTacToe skills!")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':  # Middle column win
                print_board(board)
                print("\nGame Over.\n")
                print(f"{turn} is the winner! Bow down to {turn}'s superior TicTacToe skills!")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':  # Right column win
                print_board(board)
                print("\nGame Over.\n")
                print(f"{turn} is the winner! Bow down to {turn}'s superior TicTacToe skills!")
                break
            elif board['7'] == board['5'] == board['3'] != ' ':  # Diagonal win
                print_board(board)
                print("\nGame Over.\n")
                print(f"{turn} is the winner! Bow down to {turn}'s superior TicTacToe skills!")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':  # Diagonal win
                print_board(board)
                print("\nGame Over.\n")
                print(f"{turn} is the winner! Bow down to {turn}'s superior TicTacToe skills!")
                break

        # Tie condition
        if count == 9:
            print("\nGame Over.\n")
            print("The game is tied. No winner. Play again to settle the odds.")
            quit()

        # Alternate players.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Play again?
    restart = input("Do want to play again?(y/n)")
    if restart.upper() == "Y":
        for key in board_keys:
            board[key] = " "

        game()


if __name__ == "__main__":
    game()
