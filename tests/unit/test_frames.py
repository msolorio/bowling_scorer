from app.frames import Frames
from app.frame import StrikeFrame, SpareFrame, OpenFrame
from app.throws import Throws


def test_current_frame_number_with_no_throw():
    frames = Frames(throws=Throws())

    assert frames.current_frame_number == 1


def test_current_frame_number_with_one_non_strike_throw():
    throws = Throws()
    throws.add(5)

    frames = Frames(throws=throws)

    assert frames.current_frame_number == 1


def test_current_frame_number_with_one_strike_throw():
    throws = Throws()
    throws.add(10)

    frames = Frames(throws=throws)

    assert frames.current_frame_number == 2


def test_current_frame_number_with_one_open_frame():
    throws = Throws()
    throws.add(5)
    throws.add(3)

    frames = Frames(throws=throws)

    assert frames.current_frame_number == 2


def test_create_strike_frame():
    throws = Throws()
    throws.add(10)
    throws.add(1)
    throws.add(1)

    frames = Frames(throws=throws)

    assert isinstance(frames[0], StrikeFrame)
    assert frames[0].score == 12
    assert frames[0].total_throws == 1


def test_create_spare_frame():
    throws = Throws()
    throws.add(5)
    throws.add(5)
    throws.add(3)

    frames = Frames(throws=throws)

    assert isinstance(frames[0], SpareFrame)
    assert frames[0].score == 13
    assert frames[0].total_throws == 2


def test_create_open_frame():
    throws = Throws()
    throws.add(5)
    throws.add(3)

    frames = Frames(throws=throws)

    assert isinstance(frames[0], OpenFrame)
    assert frames[0].score == 8
    assert frames[0].total_throws == 2


def test_create_incomplete_frame():
    throws = Throws()
    throws.add(5)

    frames = Frames(throws=throws)

    assert isinstance(frames[0], OpenFrame)
    assert frames[0].score == 5
    assert frames[0].total_throws == 2
    assert frames[0].is_full is False


def test_score_at_frame_number_single_open_frame():
    throws = Throws()
    throws.add(5)
    throws.add(3)
    frames = Frames(throws=throws)

    assert frames.score_at_frame(1) == 8


def test_score_at_frame_number_strike_frame():
    throws = Throws()
    throws.add(10)
    throws.add(1)
    throws.add(1)
    frames = Frames(throws=throws)

    assert frames.score_at_frame(1) == 12
    assert frames.score_at_frame(2) == 14


def test_score_at_frame_number_lone_strike_frame():
    throws = Throws()
    throws.add(10)
    frames = Frames(throws=throws)

    assert frames.score_at_frame(1) == 10
