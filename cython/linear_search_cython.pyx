# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True
# cython: nonecheck=False
# cython: initializedcheck=False
# cython: overflowcheck=False
# cython: infer_types=True
# cython: language_level=3
# cython: cdivision_warnings=False
# cython: embedsignature=True
# cython: binding=True
# cython: linetrace=False
# cython: profile=False

import numpy as np
cimport numpy as np


def linear_search_cython(np.ndarray[np.float64_t, ndim=1] a, np.ndarray[np.float64_t, ndim=1] b):
    cdef np.ndarray[np.uint64_t, ndim=1] idx = np.full(shape=b.size, fill_value=a.size, dtype=np.uint64)
    cdef Py_ssize_t i = 0
    cdef Py_ssize_t j = 0

    if a.size == 0 or b.size == 0:
        return idx

    while i < a.size and j < b.size:
        while j < b.size and b[j] < a[i]:
            idx[j] = i
            j += 1
        i += 1

    return idx
