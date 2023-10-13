import pytest

from ttt import *


def empty_board():
    return ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']


def test_play_turn():
    assert play_turn(empty_board(), 'X', at=0) == ['X', '-', '-', '-', '-', '-', '-', '-', '-']


def test_win_not_possible():
    assert count_possible_wins(empty_board(), 'O') == 0


def test_win_possible_in_a_row():
    board = ['X', 'X', '-',
             '-', 'O', '-',
             '-', '-', '-']
    assert count_possible_wins(board, 'X') == 1


def test_win_possible_in_a_column():
    board = ['X', '-', '-',
             'X', 'O', '-',
             '-', '-', '-']
    assert count_possible_wins(board, 'X') == 1


def test_win_possible_in_a_diagonal():
    board = ['X', '-', '-',
             '-', 'X', 'O',
             '-', '-', '-']
    assert count_possible_wins(board, 'X') == 1


def test_win_possible_with_fork():
    board = ['X', 'X', '-',
             'O', 'X', 'O',
             '-', 'O', '-']
    assert count_possible_wins(board, 'X') == 2


def test_best_move_in_empty_board():
    assert find_best_move(empty_board(), 'X') == 4


@pytest.mark.parametrize('board, player, expected', [
    (['X', 'X', '-',
      '-', 'O', '-',
      '-', '-', '-'], 'X', 2),
    (['X', '-', '-',
      'X', 'O', '-',
      '-', '-', '-'], 'X', 6),
    (['X', 'O', '-',
      '-', 'X', 'O',
      '-', 'O', '-'], 'X', 8),
])
def test_best_move_is_win(board, player, expected):
    assert find_best_move(board, player) == expected


@pytest.mark.parametrize('board, player, expected', [
    (['X', 'X', '-',
      '-', 'O', '-',
      '-', '-', '-'], 'O', 2),
    (['X', '-', '-',
      'X', 'O', '-',
      '-', '-', '-'], 'O', 6),
    (['X', 'O', '-',
      '-', 'X', '-',
      '-', 'O', '-'], 'O', 8),
])
def test_best_move_is_block(board, player, expected):
    assert find_best_move(board, player) == expected


@pytest.mark.parametrize('board, player, expected', [
    (['-', '-', '-',
      'X', 'X', 'O',
      '-', 'O', '-'], 'X', 0),
    (['-', '-', '-',
      'X', 'O', 'O',
      '-', 'X', '-'], 'X', 6),
])
def test_best_move_is_fork(board, player, expected):
    assert find_best_move(board, player) == expected


@pytest.mark.parametrize('board, player, expected', [
    (['-', '-', '-',
      'X', 'X', 'O',
      '-', '-', '-'], 'O', 0),
    (['-', '-', '-',
      'X', '-', 'O',
      '-', 'X', '-'], 'O', 6),
])
def test_best_move_is_block_fork(board, player, expected):
    assert find_best_move(board, player) == expected


@pytest.mark.parametrize('board, player, expected', [
    (['X', 'O', 'X',
      'X', 'O', '-',
      'O', 'X', '-'], 'O', 8),
    (['O', 'X', '-',
      'X', 'O', '-',
      'X', 'O', 'X'], 'O', 2),
])
def test_best_move_in_opposite_corner(board, player, expected):
    assert find_best_move(board, player) == expected


@pytest.mark.parametrize('board, player, expected', [
    (['-', '-', '-',
      '-', 'X', '-',
      '-', '-', '-'], 'O', 0),
    (['X', '-', '-',
      '-', 'O', '-',
      '-', '-', 'X'], 'O', 2),
])
def test_best_move_in_empty_corner(board, player, expected):
    assert find_best_move(board, player) == expected


@pytest.mark.parametrize('board, player, expected', [
    (['X', '-', 'O',
      'O', 'O', 'X',
      'X', '-', 'O'], 'O', 1),
])
def test_best_move_in_empty_side(board, player, expected):
    assert find_best_move(board, player) == expected


@pytest.mark.parametrize('board, expected', [
    (['X', '-', 'O',
      'O', 'O', 'X',
      'X', '-', 'O'], 'unfinished'),
    (['X', 'X', 'O',
      'O', 'O', 'X',
      'X', 'O', 'X'], 'draw'),
    (['X', 'X', 'O',
      'O', 'X', 'X',
      'O', 'O', 'X'], 'X'),
    (['X', '-', '-',
      'O', 'O', 'O',
      'X', '-', 'X'], 'O'),

])
def test_game_result(board, expected):
    assert game_result(board) == expected


@pytest.mark.parametrize('moves, result', [
    ({'X': [0, 8, 7, 2, 3], 'O': [4, 1, 6, 5]}, 'draw'),
    ({'X': [0, 8, 6, 3], 'O': [4, 2, 1]}, 'X'),
])
def test_game(moves, result):
    board = play_game(moves)
    assert result == game_result(board)


def play_game(game):
    board = empty_board()
    min_len = min(len(game['X']), len(game['O']))

    for i in range(min_len):
        board = play_turn(board, 'X', game['X'][i])
        board = play_turn(board, 'O', game['O'][i])

    board = play_turn(board, 'X', game['X'][-1])
    return board
