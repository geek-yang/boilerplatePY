"""Unit tests for foo."""
from boilerplatepy import foo


class TestFoo:
    def test_add(self):
        a = 1
        b = 2
        assert foo.add(a, b) == 3
