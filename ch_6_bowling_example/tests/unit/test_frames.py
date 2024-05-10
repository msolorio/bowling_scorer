from app.frames import Frames
from app.frame import StrikeFrame, SpareFrame, OpenFrame, IncompleteFrame
from app.throw import Throw


def test_current_frame_number_with_no_throw():
    frames = Frames()

    assert frames.current_frame_number == 1


def test_current_frame_number_with_one_non_strike_throw():
    frames = Frames(throws=[5], first_throw=Throw(5))

    assert frames.current_frame_number == 1


def test_current_frame_number_with_one_strike_throw():
    frames = Frames(throws=[10], first_throw=Throw(10))

    assert frames.current_frame_number == 2


def test_current_frame_number_with_one_open_frame():
    starting_throw = Throw(5)
    starting_throw.next = 3

    frames = Frames(throws=[5, 3], first_throw=starting_throw)

    assert frames.current_frame_number == 2


def test_create_strike_frame():
    throws = [10, 1, 1]
    starting_throw = Throw(10)
    starting_throw.next = 1
    starting_throw.next.next = 1

    frames = Frames(throws=throws, first_throw=starting_throw)

    assert isinstance(frames[0], StrikeFrame)
    assert frames[0].score == 12
    assert frames[0].num_of_throws == 1


def test_create_spare_frame():
    throws = [5, 5, 3]
    starting_throw = Throw(5)
    starting_throw.next = 5
    starting_throw.next.next = 3

    frames = Frames(throws=throws, first_throw=starting_throw)

    assert isinstance(frames[0], SpareFrame)
    assert frames[0].score == 13
    assert frames[0].num_of_throws == 2


def test_create_open_frame():
    throws = [5, 3]

    starting_throw = Throw(5)
    starting_throw.next = 3

    frames = Frames(throws=throws, first_throw=starting_throw)

    assert isinstance(frames[0], OpenFrame)
    assert frames[0].score == 8
    assert frames[0].num_of_throws == 2


def test_create_incomplete_frame():
    throws = [5]
    starting_throw = Throw(5)

    frames = Frames(throws=throws, first_throw=starting_throw)

    assert isinstance(frames[0], IncompleteFrame)
    assert frames[0].score == 5
    assert frames[0].num_of_throws == 1
