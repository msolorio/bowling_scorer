import pytest
from app.app import add_two_nums


def test_pytest_works():
    assert 1 == 1


def test_add_two_nums():
    assert add_two_nums(1, 2) == 3
