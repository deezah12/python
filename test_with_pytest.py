import pytest

from with_pytest import add


@pytest.fixture()
def db():
    return 5


def test_add(db):
    assert add(2, db) == 7


def test_add_with_strings():
    assert add("hello", "world")

@pytest.mark.parametrize
def test_add():
    pass

