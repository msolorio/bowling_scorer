from app.throw import Throw


def test_can_create_throw():
    throw = Throw(5)
    assert throw == 5
    assert throw.next is None


def test_can_access_throws_next_throw():
    throw = Throw(5)
    throw.next = 3
    assert throw.next == 3
    assert isinstance(throw.next, Throw)
    assert throw.second_next is None


def test_can_access_throws_next_next_throw():
    throw = Throw(5)
    throw.next = 3
    throw.next.next = 2
    assert throw.next == 3
    assert isinstance(throw.next, Throw)
    assert throw.second_next == 2
    assert isinstance(throw.second_next, Throw)


def test_can_add_two_throws():
    throw = Throw(5)
    throw.next = 3

    assert throw + throw.next == 8
