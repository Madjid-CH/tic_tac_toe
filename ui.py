import ttt


def show_board(board):
    console_board = [cell if not ttt.is_empty(cell) else str(i + 1) for i, cell in enumerate(board)]
    print(
        " {} | {} | {} \n"
        "-----------\n"
        " {} | {} | {} \n"
        "-----------\n"
        " {} | {} | {} \n\n".format(*console_board)
    )


def get_user_move():
    s = input("Enter a move: ")
    while not s.isdigit():
        s = input("Please Enter a valid move: ")
    move = int(s)
    return move - 1


def empty_board():
    return ["-"] * 9


def main():
    print("Welcome to Tic Tac Toe!.")
    while True:
        print("If you want to start first enter 'x' else enter 'o'")
        player = input("Enter your choice: ")
        while player not in ["x", "o"]:
            print("Invalid input, please enter 'x' or 'o'")
            player = input("Enter your choice: ")
            continue
        player = player.upper()
        board = empty_board()
        print("You are playing as ", player)
        show_board(board)
        play_game(board, player)
        print("\n\n do you want to continue? (y/n)")
        choice = input("Enter your choice: ")
        if choice == 'y':
            continue
        else:
            break


def play_game(board, player):
    turn = 'X'
    while ttt.game_result(board) == 'unfinished':
        if player == turn:
            print("Your turn")
            move = get_user_move()
            if not is_valid(board, move):
                print("Invalid move please try again")
                continue
            board = ttt.play_turn(board, player, move)
        else:
            print("Computer's turn")
            move = ttt.find_best_move(board, turn)
            board = ttt.play_turn(board, turn, move)
        show_board(board)
        turn = ttt.opponent(turn)
    print_message(board)


def is_valid(board, move):
    return 0 <= move < 9 and board[move] == '-'


def print_message(board):
    result = ttt.game_result(board)
    if result == 'draw':
        print("Game over. Result: ", result)
    else:
        print("Game over. Result: ", result, "wins")


if __name__ == '__main__':
    main()
