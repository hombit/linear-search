from functools import partial

import numpy as np
import pytest
from numpy.testing import assert_array_equal

from linear_search_cython import linear_search_cython as cython
from linear_search_numba import linear_search_numba as numba
from linear_search_pure import linear_search_pure as pure
# from linear_search_rust import linear_search_rust as rust
from linear_search_rust import linear_search_rust_noboundscheck as rust


searchsorted_right = partial(np.searchsorted, side='right')
searchsorted_right.__name__ = 'np_searchsorted'


# searchsorted_right is just for benchmark comparison
@pytest.mark.parametrize("f", [cython, numba, pure, rust, searchsorted_right])
@pytest.mark.parametrize("n1", [0, 1, 1000, 1_000_000])
@pytest.mark.parametrize("n2", [0, 1, 1000, 1_000_000])
def test_random(benchmark, f, n1, n2):
    benchmark.group = f'{n1 = }, {n2 = }'

    rng = np.random.default_rng(n1 + n2)
    a = np.sort(rng.normal(0, 1, size=n1))
    b = np.sort(rng.normal(0, 1, size=n2))

    expected = searchsorted_right(a, b, side='right')
    actual = benchmark(f, a, b)

    assert_array_equal(actual, expected)


@pytest.mark.parametrize("f", [cython, numba, pure, rust])
def test_right_side(f):
    a = np.arange(10.0)
    b = np.linspace(-10.0, 10.0, 201)

    expected = np.searchsorted(a, b, side='right')
    actual = f(a, b)

    assert_array_equal(actual, expected)
