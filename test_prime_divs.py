#!/usr/bin/env python3

"""Module de test de prime_divs.py

Lancez les tests avec :
	$ python3 -m pytest
Si vous avez une erreur, installez d'abord pytest :
	$ pip3 install -U pytest
"""


from prime_divs import *
import pytest

@pytest.mark.parametrize("number, i, expected", [
	(10, 2, True),
	(5, 5, True),
	(3, 2, False),
	(15, 4, False),
])
def test_is_div(number, i, expected):
	assert is_div(number, i) == expected

@pytest.mark.parametrize("number, expected", [
	(2, True),
	(4, False),
	(13, True),
	(97, True),
	(100, False),
])
def test_is_prime(number, expected):
	assert is_prime(number) == expected

@pytest.mark.parametrize("number, expected", [
	(10, [2, 5]),
	(100, [2, 5]),
	(13, []),
	(432, [2, 3]),
	(291, [3, 97]),
])
def test_prime_divs(number, expected):
	assert prime_divs(number) == expected
