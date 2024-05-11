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


def test_score_with_two_strikes_and_incomplete_frame(new_game):
    game = new_game
    game.add_throw(10)
    game.add_throw(10)
    game.add_throw(1)
    assert game.score == 33
    assert game.current_frame_number == 3


def test_score_with_lone_strike(new_game):
    game = new_game
    game.add_throw(10)
    assert game.score == 10
    assert game.current_frame_number == 2


def test_score_with_strike_and_incomplete_frame(new_game):
    game = new_game
    game.add_throw(10)
    game.add_throw(1)
    assert game.score == 12
    assert game.current_frame_number == 2


def test_score_with_lone_spare(new_game):
    game = new_game
    game.add_throw(5)
    game.add_throw(5)
    assert game.score == 10
    assert game.current_frame_number == 2


def test_score_with_spare_and_strike(new_game):
    game = new_game
    game.add_throw(5)
    game.add_throw(5)
    game.add_throw(10)
    game.add_throw(1)
    assert game.score == 32
    assert game.current_frame_number == 3


def test_score_strike_and_spare(new_game):
    game = new_game
    game.add_throw(10)
    game.add_throw(5)
    game.add_throw(5)
    game.add_throw(1)
    assert game.score == 32
    assert game.current_frame_number == 3


def test_score_perfect_game(new_game):
    game = new_game
    for _ in range(12):
        game.add_throw(10)
    assert game.score == 300
    assert game.current_frame_number == 11


def test_score_full_game_open_frames(new_game):
    game = new_game
    for _ in range(20):
        game.add_throw(1)
    assert game.score == 20
    assert game.current_frame_number == 11


def test_score_incomplete_final_strike_frame(new_game):
    game = new_game
    for _ in range(18):
        game.add_throw(1)
    game.add_throw(10)
    assert game.score == 28
    assert game.current_frame_number == 10


def test_score_incomplete_final_frame(new_game):
    game = new_game
    for _ in range(19):
        game.add_throw(1)
    assert game.score == 19
    assert game.current_frame_number == 10
