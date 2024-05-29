from app.throw import ThrowNode, EmptyNode


def test_can_create_throw():
    throw = ThrowNode(5)
    assert throw == 5
    assert isinstance(throw.next, EmptyNode)


def test_can_access_throws_next_throw():
    throw = ThrowNode(5)
    throw.next = 3
    assert throw.next == 3
    assert isinstance(throw.next, ThrowNode)
    assert isinstance(throw.second_next, EmptyNode)


def test_can_access_throws_next_next_throw():
    throw = ThrowNode(5)
    throw.next = 3
    throw.next.next = 2
    assert throw.next == 3
    assert isinstance(throw.next, ThrowNode)
    assert throw.second_next == 2
    assert isinstance(throw.second_next, ThrowNode)


def test_can_add_two_throws():
    throw = ThrowNode(5)
    throw.next = 3

    assert throw + throw.next == 8


def test_can_add_throw_with_empty_node():
    throw = ThrowNode(5)
    assert isinstance(throw.next, EmptyNode)
    assert throw + throw.next == 5


def test_throw_is_strike_throw():
    throw = ThrowNode(10)
    assert throw.is_strike


def test_throw_is_spare_throw():
    throw = ThrowNode(5)
    throw.next = 5
    assert not throw.is_strike
    assert throw.is_spare


def test_throw_has_one_later_throw():
    throw = ThrowNode(5)
    throw.next = 3
    assert throw.num_of_later_throws == 1


def test_throw_has_two_later_throw():
    throw = ThrowNode(5)
    throw.next = 3
    throw.next.next = 2
    assert throw.num_of_later_throws == 2


def test_throw_can_get_1st_later_throw():
    throw = ThrowNode(5)
    throw.next = 3
    assert throw.xth_later_throw(1) == 3


def test_throw_can_get_2nd_later_throw():
    throw = ThrowNode(5)
    throw.next = 3
    throw.next.next = 7
    assert throw.xth_later_throw(2) == 7
