import numpy as np
from numba import uint64, float64, njit
from numpy.typing import NDArray


@njit(uint64[:](float64[:], float64[:]), boundscheck=False, fastmath=True)
def linear_search_numba(a: NDArray, b: NDArray) -> NDArray:
    """Find the place index of each element of b in a. Both a and b are sorted."""

    # Initialize the index with the last index of the target array
    idx = np.full(shape=b.size, fill_value=a.size, dtype=np.uint64)

    if a.size == 0 or b.size == 0:
        return idx

    i = 0
    j = 0

    while i < a.size and j < b.size:
        while j < b.size and b[j] < a[i]:
            idx[j] = i
            j += 1
        i += 1

    return idx
