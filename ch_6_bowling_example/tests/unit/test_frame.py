from app.frame import Frame
from app.game import Frame_2


def test_get_frame_score_with_no_throws():
    frame = Frame()
    assert frame.score() == 0


def test_get_frame_score_with_one_throw():
    frame = Frame()
    frame.add_throw(5)
    assert frame.score() == 5
