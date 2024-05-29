from app.throws import Throws
from app.throw import EmptyNode


def test_can_add_and_access_single_throw():
    throws = Throws()
    throws.add(5)

    assert throws.first == 5
    assert isinstance(throws.first.next, EmptyNode)


def test_can_add_and_access_two_throws():
    throws = Throws()
    throws.add(5)
    throws.add(3)

    assert throws.first == 5
    assert throws.first.next == 3
