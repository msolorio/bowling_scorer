from app.frame import Frame


def test_get_frame_score_with_no_throws():
    frame = Frame()
    assert frame.get_score() == 0
