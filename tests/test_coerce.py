import pytest
from coerce import coerce


def test_sanity():
    @coerce()
    def example(number: int) -> None:
        assert isinstance(number, int)

    example(number="1")
