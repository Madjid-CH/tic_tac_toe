def play_turn(board, player, at):
    board[at] = player
    return board


def game_result(board):
    if is_winner(board, 'X'):
        return 'X'
    elif is_winner(board, 'O'):
        return 'O'
    elif is_draw(board):
        return 'draw'
    else:
        return 'unfinished'


def is_winner(board, player):
    lines = get_rows(board) + get_columns(board) + get_diagonals(board)
    for line in lines:
        if line.count(player) == 3:
            return True
    return False


def is_draw(board):
    return '-' not in board


def first(*args):
    for arg in args:
        if arg is not None:
            return arg


def find_best_move(board, player):
    return first(
        win(board, player),
        block(board, player),
        fork(board, player),
        block_fork(board, player),
        center(board, player),
        opposite_corner(board, player),
        empty_corner(board, player),
        empty_side(board, player),

    )


def win(board, player):
    return first(
        find_win_index(get_rows(board), player, get_index_from_row),
        find_win_index(get_columns(board), player, get_index_from_column),
        find_win_index(get_diagonals(board), player, get_index_from_diagonal)
    )


def block(board, player):
    return win(board, opponent(player))


def opponent(player):
    return 'O' if player == 'X' else 'X'


def fork(board, player):
    for i, cell in enumerate(board):
        if is_empty(cell):
            new_board = board.copy()
            new_board[i] = player
            if count_possible_wins(new_board, player) == 2:
                return i
    return None


def block_fork(board, player):
    return fork(board, opponent(player))


def opposite_corner(board, player):
    corners = (0, 2, 6, 8)
    for corner in corners:
        if board[corner] == opponent(player):
            if is_empty(board[8 - corner]):
                return 8 - corner
            else:
                return None
    return None


def empty_corner(board, _player):
    corners = (0, 2, 6, 8)
    for corner in corners:
        if is_empty(board[corner]):
            return corner
    return None


def empty_side(board, _player):
    sides = (1, 3, 5, 7)
    for side in sides:
        if is_empty(board[side]):
            return side
    return None


def is_empty(cell):
    return cell == '-'


def find_win_index(lines, player, get_index_fn):
    for i, line in enumerate(lines):
        if line.count(player) == 2 and line.count('-') == 1:
            return get_index_fn(line, i)
    return None


def get_index_from_diagonal(diagonal, i):
    if i == 0:
        index = diagonal.index('-') * 4
    else:
        index = 2 + diagonal.index('-') * 2
    return index


def get_index_from_column(column, i):
    return column.index('-') * 3 + i


def get_index_from_row(row, i):
    return i * 3 + row.index('-')


def center(board, _player):
    return 4 if is_empty(board[4]) else None


def count_possible_wins(board, player):
    count = 0
    lines = get_rows(board) + get_columns(board) + get_diagonals(board)
    for line in lines:
        if line.count(player) == 2 and line.count('-') == 1:
            count += 1
    return count


def get_rows(board):
    return board[0:3], board[3:6], board[6:9]


def get_columns(board):
    return board[0:9:3], board[1:9:3], board[2:9:3]


def get_diagonals(board):
    return board[0:9:4], board[2:7:2]
