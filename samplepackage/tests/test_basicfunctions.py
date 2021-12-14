import unittest

import pytest
from samplepackage import day_evaluator, make_me_feel_bad, make_me_happy


def test_make_me_happy():
    result = make_me_happy()
    assert result == "Today is Saturday!"


def test_make_me_feel_bad():
    result = make_me_feel_bad()
    assert result == "Tomorrow is Monday... :("


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Monday", 2),
        ("Tuesday", 2),
        ("Wednesday", 6),
        ("Thursday", 6),
        ("Friday", 8),
        ("Saturday", 10),
        ("Sunday", 7)
    ]
)
def test_day_evaluator(test_input, expected):
    result = day_evaluator(test_input)
    assert result == expected


def test_day_evaluator_raise_exception():
    unittest.TestCase().assertRaises(
        ValueError, day_evaluator, "January"
    )
