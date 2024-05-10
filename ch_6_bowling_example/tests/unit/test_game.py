import pytest
from app.game import Game as Game
from app.frame import StrikeFrame, OpenFrame


@pytest.fixture
def new_game():
    yield Game()


def test_score_with_no_throws(new_game):
    game = new_game
    assert game.score == 0
    assert game.current_frame_number == 1


def test_score_with_one_throw(new_game):
    game = new_game
    game.add_throw(5)
    assert game.score == 5
    assert game.current_frame_number == 1


def test_score_with_two_throws(new_game):
    game = new_game
    game.add_throw(5)
    game.add_throw(4)
    assert game.score == 9
    assert game.current_frame_number == 2


def test_score_with_four_throws_no_marks(new_game):
    game = new_game
    game.add_throw(5)
    game.add_throw(4)
    game.add_throw(7)
    game.add_throw(2)
    assert game.score == 18
    assert game.score_at_frame(1) == 9
    assert game.score_at_frame(2) == 18
    assert game.current_frame_number == 3


def test_score_with_spare(new_game):
    game = new_game
    game.add_throw(3)
    game.add_throw(7)
    game.add_throw(3)
    assert game.score == 16
    assert game.score_at_frame(1) == 13
    assert game.current_frame_number == 2


def test_score_with_strike(new_game):
    game = new_game
    game.add_throw(10)
    game.add_throw(1)
    game.add_throw(1)
    assert game.score == 14
    assert game.score_at_frame(1) == 12
    assert game.score_at_frame(2) == 14
    assert game.current_frame_number == 3


def test_score_with_two_strikes(new_game):
    game = new_game
    game.add_throw(10)
    game.add_throw(10)
    game.add_throw(1)
    game.add_throw(1)
    assert game.score == 35


# def test_score_perfect_game(new_game):
#     game = new_game
#     for _ in range(12):
#         game.add_throw(10)
#     assert game.score == 300
#     assert game.current_frame_number == 11
