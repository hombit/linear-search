# Linear search in Python

## Multiple implementations of linear search in Python

Implemented in:
- `./python/` — pure Python implementation
- `./cython/` — Cython implementation
- `./numba/` — Numba implementation
- `./rust/` — Rust implementation, includes "unsafe" version with no bound checks, which gives ≲1% of performance boost

### Benchmark results

Prepare environment and install packages:
```bash
# Create virtual environment
python3 -mvenv venv
source venv/bin/activate
python --m pip install pytest-benchmark
# Install packages
python -m pip install -e ./cython
python -m pip install -e ./numba
python -m pip install -e ./python
python -m pip install -e ./rust
```

Run benchmark:
```bash
python -m pytest --benchmark-columns=mean,stddev --benchmark-sort=mean
```

Results on Macbook M2Pro:
```
------------------------------- benchmark 'n1 = 0, n2 = 0': 4 tests -------------------------------
Name (time in ns)                                                Mean              StdDev
---------------------------------------------------------------------------------------------------
test_linear_search[0-0-linear_search_rust_noboundscheck]     327.3206 (1.0)      235.0193 (2.42)
test_linear_search[0-0-linear_search_numba]                  393.2957 (1.20)      97.1597 (1.0)
test_linear_search[0-0-linear_search_pure]                   586.4697 (1.79)     150.3064 (1.55)
test_linear_search[0-0-linear_search_cython]                 808.8742 (2.47)     270.9800 (2.79)
---------------------------------------------------------------------------------------------------

------------------------------- benchmark 'n1 = 0, n2 = 1': 4 tests -------------------------------
Name (time in ns)                                                Mean              StdDev
---------------------------------------------------------------------------------------------------
test_linear_search[1-0-linear_search_rust_noboundscheck]     336.6778 (1.0)      102.4995 (1.45)
test_linear_search[1-0-linear_search_numba]                  401.6889 (1.19)     465.6984 (6.59)
test_linear_search[1-0-linear_search_pure]                   593.4684 (1.76)      70.6428 (1.0)
test_linear_search[1-0-linear_search_cython]                 808.8178 (2.40)     569.3157 (8.06)
---------------------------------------------------------------------------------------------------

--------------------------------- benchmark 'n1 = 0, n2 = 1000': 4 tests ---------------------------------
Name (time in ns)                                                     Mean                StdDev
----------------------------------------------------------------------------------------------------------
test_linear_search[1000-0-linear_search_rust_noboundscheck]       472.4067 (1.0)        754.2321 (1.0)
test_linear_search[1000-0-linear_search_numba]                    592.7882 (1.25)       934.5111 (1.24)
test_linear_search[1000-0-linear_search_pure]                     942.4448 (1.99)     1,265.1639 (1.68)
test_linear_search[1000-0-linear_search_cython]                 1,112.5193 (2.36)     1,709.6834 (2.27)
----------------------------------------------------------------------------------------------------------

------------------------------- benchmark 'n1 = 0, n2 = 1000000': 4 tests -------------------------------
Name (time in us)                                                      Mean              StdDev
---------------------------------------------------------------------------------------------------------
test_linear_search[1000000-0-linear_search_rust_noboundscheck]     408.5258 (1.0)       65.1147 (1.0)
test_linear_search[1000000-0-linear_search_numba]                  542.4217 (1.33)     122.6432 (1.88)
test_linear_search[1000000-0-linear_search_pure]                   546.2315 (1.34)      98.8458 (1.52)
test_linear_search[1000000-0-linear_search_cython]                 583.0861 (1.43)     162.0187 (2.49)
---------------------------------------------------------------------------------------------------------

------------------------------- benchmark 'n1 = 1, n2 = 0': 4 tests -------------------------------
Name (time in ns)                                                Mean              StdDev
---------------------------------------------------------------------------------------------------
test_linear_search[0-1-linear_search_rust_noboundscheck]     313.1247 (1.0)      124.3591 (1.41)
test_linear_search[0-1-linear_search_numba]                  398.2908 (1.27)     156.6335 (1.78)
test_linear_search[0-1-linear_search_pure]                   595.3588 (1.90)      88.0974 (1.0)
test_linear_search[0-1-linear_search_cython]                 816.4009 (2.61)     433.4784 (4.92)
---------------------------------------------------------------------------------------------------

------------------------------- benchmark 'n1 = 1, n2 = 1': 4 tests -------------------------------
Name (time in ns)                                                Mean              StdDev
---------------------------------------------------------------------------------------------------
test_linear_search[1-1-linear_search_rust_noboundscheck]     340.3441 (1.0)      253.5676 (1.0)
test_linear_search[1-1-linear_search_numba]                  402.7589 (1.18)     446.9103 (1.76)
test_linear_search[1-1-linear_search_cython]                 820.7532 (2.41)     539.9627 (2.13)
test_linear_search[1-1-linear_search_pure]                   912.0485 (2.68)     680.2992 (2.68)
---------------------------------------------------------------------------------------------------

----------------------------------- benchmark 'n1 = 1, n2 = 1000': 4 tests ----------------------------------
Name (time in ns)                                                       Mean                 StdDev
-------------------------------------------------------------------------------------------------------------
test_linear_search[1000-1-linear_search_rust_noboundscheck]         755.4727 (1.0)         454.7389 (1.0)
test_linear_search[1000-1-linear_search_numba]                    1,271.0110 (1.68)      1,227.1650 (2.70)
test_linear_search[1000-1-linear_search_cython]                   2,409.0445 (3.19)      2,008.5260 (4.42)
test_linear_search[1000-1-linear_search_pure]                   133,563.6183 (176.79)   22,197.2780 (48.81)
-------------------------------------------------------------------------------------------------------------

---------------------------------- benchmark 'n1 = 1, n2 = 1000000': 4 tests ----------------------------------
Name (time in us)                                                          Mean                StdDev
---------------------------------------------------------------------------------------------------------------
test_linear_search[1000000-1-linear_search_rust_noboundscheck]         867.1760 (1.0)        157.9773 (1.45)
test_linear_search[1000000-1-linear_search_numba]                    1,239.6231 (1.43)       108.7769 (1.0)
test_linear_search[1000000-1-linear_search_cython]                   1,800.4159 (2.08)       153.6166 (1.41)
test_linear_search[1000000-1-linear_search_pure]                   128,355.5884 (148.02)   1,071.6189 (9.85)
---------------------------------------------------------------------------------------------------------------

------------------------------- benchmark 'n1 = 1000, n2 = 0': 4 tests -------------------------------
Name (time in ns)                                                   Mean              StdDev
------------------------------------------------------------------------------------------------------
test_linear_search[0-1000-linear_search_rust_noboundscheck]     316.8144 (1.0)       71.4854 (1.0)
test_linear_search[0-1000-linear_search_numba]                  396.1025 (1.25)     541.5285 (7.58)
test_linear_search[0-1000-linear_search_pure]                   612.4932 (1.93)      73.5979 (1.03)
test_linear_search[0-1000-linear_search_cython]                 829.2752 (2.62)     677.4657 (9.48)
------------------------------------------------------------------------------------------------------

---------------------------------- benchmark 'n1 = 1000, n2 = 1': 4 tests ----------------------------------
Name (time in ns)                                                       Mean                StdDev
------------------------------------------------------------------------------------------------------------
test_linear_search[1-1000-linear_search_rust_noboundscheck]         807.6801 (1.0)         77.5351 (1.0)
test_linear_search[1-1000-linear_search_numba]                    1,014.9053 (1.26)       401.2935 (5.18)
test_linear_search[1-1000-linear_search_cython]                   4,107.3950 (5.09)       673.4224 (8.69)
test_linear_search[1-1000-linear_search_pure]                   123,178.5947 (152.51)   7,775.5807 (100.28)
------------------------------------------------------------------------------------------------------------

------------------------------ benchmark 'n1 = 1000, n2 = 1000': 4 tests -------------------------------
Name (time in us)                                                      Mean             StdDev
--------------------------------------------------------------------------------------------------------
test_linear_search[1000-1000-linear_search_numba]                    1.9625 (1.0)       0.7479 (1.0)
test_linear_search[1000-1000-linear_search_rust_noboundscheck]       2.0603 (1.05)      1.9226 (2.57)
test_linear_search[1000-1000-linear_search_cython]                  10.4088 (5.30)      1.3775 (1.84)
test_linear_search[1000-1000-linear_search_pure]                   349.8981 (178.30)   35.6772 (47.70)
--------------------------------------------------------------------------------------------------------

------------------------------ benchmark 'n1 = 1000, n2 = 1000000': 4 tests ------------------------------
Name (time in ms)                                                         Mean            StdDev
----------------------------------------------------------------------------------------------------------
test_linear_search[1000000-1000-linear_search_rust_noboundscheck]       1.0681 (1.0)      0.2292 (1.21)
test_linear_search[1000000-1000-linear_search_numba]                    1.4846 (1.39)     0.1892 (1.0)
test_linear_search[1000000-1000-linear_search_cython]                   2.2020 (2.06)     0.2670 (1.41)
test_linear_search[1000000-1000-linear_search_pure]                   167.8315 (157.13)   1.3977 (7.39)
----------------------------------------------------------------------------------------------------------

------------------------------- benchmark 'n1 = 1000000, n2 = 0': 4 tests -------------------------------
Name (time in ns)                                                      Mean              StdDev
---------------------------------------------------------------------------------------------------------
test_linear_search[0-1000000-linear_search_rust_noboundscheck]     316.3546 (1.0)      139.5537 (1.05)
test_linear_search[0-1000000-linear_search_numba]                  398.0426 (1.26)     173.4129 (1.30)
test_linear_search[0-1000000-linear_search_pure]                   663.9612 (2.10)     133.0195 (1.0)
test_linear_search[0-1000000-linear_search_cython]                 817.9177 (2.59)     224.4044 (1.69)
---------------------------------------------------------------------------------------------------------

---------------------------------- benchmark 'n1 = 1000000, n2 = 1': 4 tests ----------------------------------
Name (time in us)                                                          Mean                StdDev
---------------------------------------------------------------------------------------------------------------
test_linear_search[1-1000000-linear_search_rust_noboundscheck]         515.8570 (1.0)         20.5927 (1.0)
test_linear_search[1-1000000-linear_search_numba]                      624.7939 (1.21)       121.3803 (5.89)
test_linear_search[1-1000000-linear_search_cython]                   3,367.5680 (6.53)       115.5861 (5.61)
test_linear_search[1-1000000-linear_search_pure]                   129,123.1929 (250.31)   1,521.5248 (73.89)
---------------------------------------------------------------------------------------------------------------

---------------------------------- benchmark 'n1 = 1000000, n2 = 1000': 4 tests ----------------------------------
Name (time in us)                                                             Mean                StdDev
------------------------------------------------------------------------------------------------------------------
test_linear_search[1000-1000000-linear_search_rust_noboundscheck]         634.2076 (1.0)         65.0161 (1.0)
test_linear_search[1000-1000000-linear_search_numba]                      875.3904 (1.38)       131.2516 (2.02)
test_linear_search[1000-1000000-linear_search_cython]                   4,118.1425 (6.49)       293.4602 (4.51)
test_linear_search[1000-1000000-linear_search_pure]                   166,857.3037 (263.10)   2,905.2787 (44.69)
------------------------------------------------------------------------------------------------------------------

------------------------------ benchmark 'n1 = 1000000, n2 = 1000000': 4 tests ------------------------------
Name (time in ms)                                                            Mean            StdDev
-------------------------------------------------------------------------------------------------------------
test_linear_search[1000000-1000000-linear_search_rust_noboundscheck]       9.7794 (1.0)      0.3156 (1.0)
test_linear_search[1000000-1000000-linear_search_numba]                   10.9581 (1.12)     0.3963 (1.26)
test_linear_search[1000000-1000000-linear_search_cython]                  15.4562 (1.58)     0.4867 (1.54)
test_linear_search[1000000-1000000-linear_search_pure]                   348.2351 (35.61)    2.6291 (8.33)
-------------------------------------------------------------------------------------------------------------
```
