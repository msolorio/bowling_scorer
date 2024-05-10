from app.throw import Throw, EmptyNode


def test_can_create_throw():
    throw = Throw(5)
    assert throw == 5
    assert isinstance(throw.next, EmptyNode)


def test_can_access_throws_next_throw():
    throw = Throw(5)
    throw.next = 3
    assert throw.next == 3
    assert isinstance(throw.next, Throw)
    assert isinstance(throw.second_next, EmptyNode)


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


def test_can_add_throw_with_empty_node():
    throw = Throw(5)
    assert isinstance(throw.next, EmptyNode)
    assert throw + throw.next == 5
