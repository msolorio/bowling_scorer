from app.frames import Frames
from app.frame import StrikeFrame, SpareFrame, OpenFrame, IncompleteFrame


def test_create_strike_frame():
    throws = [10, 1, 1]
    frames = Frames(throws=throws)

    assert isinstance(frames[0], StrikeFrame)
    assert frames[0].score == 12


def test_create_spare_frame():
    throws = [5, 5, 3]
    frames = Frames(throws=throws)

    assert isinstance(frames[0], SpareFrame)
    assert frames[0].score == 13


def test_create_open_frame():
    throws = [5, 3]
    frames = Frames(throws=throws)

    assert isinstance(frames[0], OpenFrame)
    assert frames[0].score == 8


def test_create_incomplete_frame():
    throws = [5]
    frames = Frames(throws=throws)

    assert isinstance(frames[0], IncompleteFrame)
    assert frames[0].score == 5
