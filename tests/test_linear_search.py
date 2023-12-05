import numpy as np
import pytest
from numpy.testing import assert_array_equal

from linear_search_cython import linear_search_cython as cython
from linear_search_numba import linear_search_numba as numba
from linear_search_pure import linear_search_pure as pure
# from linear_search_rust import linear_search_rust as rust
from linear_search_rust import linear_search_rust_noboundscheck as rust


@pytest.mark.parametrize("f", [cython, numba, pure, rust])
@pytest.mark.parametrize("n1", [0, 1, 1000, 1_000_000])
@pytest.mark.parametrize("n2", [0, 1, 1000, 1_000_000])
def test_linear_search(benchmark, f, n1, n2):
    benchmark.group = f'{n1 = }, {n2 = }'

    rng = np.random.default_rng(n1 + n2)
    a = np.sort(rng.normal(0, 1, size=n1))
    b = np.sort(rng.normal(0, 1, size=n2))

    expected = np.searchsorted(a, b)
    actual = benchmark(f, a, b)

    assert_array_equal(actual, expected)
