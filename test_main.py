import main
import numpy as np
import pytest


def test_add():
	assert(add(1, 2) == 3)


def test_get_zero_matrix():
	assert(get_zero_matrix(3) == np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
