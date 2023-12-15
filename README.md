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
--------------------------- benchmark 'n1 = 0, n2 = 0': 5 tests ----------------------------
Name (time in ns)                                         Mean              StdDev
--------------------------------------------------------------------------------------------
test_random[0-0-linear_search_rust_noboundscheck]     339.6194 (1.0)      108.8312 (3.49)
test_random[0-0-linear_search_numba]                  390.5817 (1.15)     178.5697 (5.72)
test_random[0-0-np_searchsorted]                      526.2229 (1.55)      48.2097 (1.55)
test_random[0-0-linear_search_pure]                   587.2055 (1.73)      31.2013 (1.0)
test_random[0-0-linear_search_cython]                 814.8187 (2.40)     148.5344 (4.76)
--------------------------------------------------------------------------------------------

--------------------------- benchmark 'n1 = 0, n2 = 1': 5 tests ----------------------------
Name (time in ns)                                         Mean              StdDev
--------------------------------------------------------------------------------------------
test_random[1-0-linear_search_rust_noboundscheck]     360.7630 (1.0)      106.0214 (2.39)
test_random[1-0-linear_search_numba]                  404.8671 (1.12)     229.9952 (5.18)
test_random[1-0-np_searchsorted]                      528.0389 (1.46)      51.9852 (1.17)
test_random[1-0-linear_search_pure]                   604.6312 (1.68)      44.3989 (1.0)
test_random[1-0-linear_search_cython]                 821.7900 (2.28)     237.7039 (5.35)
--------------------------------------------------------------------------------------------

----------------------------- benchmark 'n1 = 0, n2 = 1000': 5 tests ----------------------------
Name (time in ns)                                              Mean              StdDev
-------------------------------------------------------------------------------------------------
test_random[1000-0-linear_search_rust_noboundscheck]       496.4859 (1.0)      168.1557 (3.60)
test_random[1000-0-linear_search_numba]                    549.5571 (1.11)     260.7167 (5.59)
test_random[1000-0-linear_search_pure]                     808.0275 (1.63)      46.6623 (1.0)
test_random[1000-0-linear_search_cython]                 1,059.6019 (2.13)     315.8147 (6.77)
test_random[1000-0-np_searchsorted]                      1,839.4599 (3.70)     221.9672 (4.76)
-------------------------------------------------------------------------------------------------

---------------------------- benchmark 'n1 = 0, n2 = 1000000': 5 tests ----------------------------
Name (time in us)                                                 Mean             StdDev
---------------------------------------------------------------------------------------------------
test_random[1000000-0-linear_search_rust_noboundscheck]       451.3591 (1.0)      81.0664 (1.0)
test_random[1000000-0-linear_search_numba]                    514.6513 (1.14)     82.6470 (1.02)
test_random[1000000-0-linear_search_pure]                     524.0535 (1.16)     88.3341 (1.09)
test_random[1000000-0-linear_search_cython]                   533.6643 (1.18)     96.6155 (1.19)
test_random[1000000-0-np_searchsorted]                      1,657.2208 (3.67)     85.4011 (1.05)
---------------------------------------------------------------------------------------------------

--------------------------- benchmark 'n1 = 1, n2 = 0': 5 tests ----------------------------
Name (time in ns)                                         Mean              StdDev
--------------------------------------------------------------------------------------------
test_random[0-1-linear_search_rust_noboundscheck]     343.8103 (1.0)      127.5148 (3.52)
test_random[0-1-linear_search_numba]                  401.9221 (1.17)     205.2635 (5.67)
test_random[0-1-np_searchsorted]                      526.6139 (1.53)      49.0353 (1.35)
test_random[0-1-linear_search_pure]                   615.8211 (1.79)      36.2017 (1.0)
test_random[0-1-linear_search_cython]                 816.5837 (2.38)     215.6150 (5.96)
--------------------------------------------------------------------------------------------

--------------------------- benchmark 'n1 = 1, n2 = 1': 5 tests ----------------------------
Name (time in ns)                                         Mean              StdDev
--------------------------------------------------------------------------------------------
test_random[1-1-linear_search_rust_noboundscheck]     362.3157 (1.0)       33.1371 (1.0)
test_random[1-1-linear_search_numba]                  416.7252 (1.15)     205.3709 (6.20)
test_random[1-1-np_searchsorted]                      530.6849 (1.46)      46.4057 (1.40)
test_random[1-1-linear_search_cython]                 834.0820 (2.30)     209.3378 (6.32)
test_random[1-1-linear_search_pure]                   836.1345 (2.31)      93.0276 (2.81)
--------------------------------------------------------------------------------------------

------------------------------- benchmark 'n1 = 1, n2 = 1000': 5 tests ------------------------------
Name (time in ns)                                                Mean                StdDev
-----------------------------------------------------------------------------------------------------
test_random[1000-1-linear_search_rust_noboundscheck]         774.5616 (1.0)        259.6886 (1.0)
test_random[1000-1-linear_search_numba]                    1,196.9010 (1.55)       432.5245 (1.67)
test_random[1000-1-linear_search_cython]                   2,277.8249 (2.94)       377.8110 (1.45)
test_random[1000-1-np_searchsorted]                        2,888.2325 (3.73)       275.3711 (1.06)
test_random[1000-1-linear_search_pure]                   110,729.3463 (142.96)   3,124.3429 (12.03)
-----------------------------------------------------------------------------------------------------

------------------------------ benchmark 'n1 = 1, n2 = 1000000': 5 tests -------------------------------
Name (time in us)                                                   Mean                StdDev
--------------------------------------------------------------------------------------------------------
test_random[1000000-1-linear_search_rust_noboundscheck]         855.9420 (1.0)         91.8085 (1.39)
test_random[1000000-1-linear_search_numba]                    1,244.8770 (1.45)       114.6359 (1.74)
test_random[1000000-1-linear_search_cython]                   1,742.7948 (2.04)       238.8857 (3.63)
test_random[1000000-1-np_searchsorted]                        2,653.8976 (3.10)        65.8866 (1.0)
test_random[1000000-1-linear_search_pure]                   110,977.0751 (129.65)   1,563.5847 (23.73)
--------------------------------------------------------------------------------------------------------

---------------------------- benchmark 'n1 = 1000, n2 = 0': 5 tests ---------------------------
Name (time in ns)                                            Mean              StdDev
-----------------------------------------------------------------------------------------------
test_random[0-1000-linear_search_rust_noboundscheck]     345.5767 (1.0)      137.9347 (3.33)
test_random[0-1000-linear_search_numba]                  401.0349 (1.16)     262.9576 (6.36)
test_random[0-1000-np_searchsorted]                      527.8698 (1.53)      57.7568 (1.40)
test_random[0-1000-linear_search_pure]                   614.6859 (1.78)      41.3778 (1.0)
test_random[0-1000-linear_search_cython]                 821.3021 (2.38)     291.1268 (7.04)
-----------------------------------------------------------------------------------------------

------------------------------- benchmark 'n1 = 1000, n2 = 1': 5 tests ------------------------------
Name (time in ns)                                                Mean                StdDev
-----------------------------------------------------------------------------------------------------
test_random[1-1000-np_searchsorted]                          566.5439 (1.0)         59.8944 (1.0)
test_random[1-1000-linear_search_rust_noboundscheck]         866.9993 (1.53)       246.9589 (4.12)
test_random[1-1000-linear_search_numba]                    1,033.3153 (1.82)       259.3776 (4.33)
test_random[1-1000-linear_search_cython]                   3,966.8451 (7.00)       417.0161 (6.96)
test_random[1-1000-linear_search_pure]                   105,571.0441 (186.34)   3,211.9783 (53.63)
-----------------------------------------------------------------------------------------------------

-------------------------- benchmark 'n1 = 1000, n2 = 1000': 5 tests ---------------------------
Name (time in us)                                               Mean            StdDev
------------------------------------------------------------------------------------------------
test_random[1000-1000-linear_search_numba]                    1.8918 (1.0)      0.3651 (2.28)
test_random[1000-1000-linear_search_rust_noboundscheck]       1.9414 (1.03)     0.1601 (1.0)
test_random[1000-1000-linear_search_cython]                  10.1248 (5.35)     0.7542 (4.71)
test_random[1000-1000-np_searchsorted]                       58.7142 (31.04)    1.9418 (12.13)
test_random[1000-1000-linear_search_pure]                   306.1571 (161.83)   5.9321 (37.06)
------------------------------------------------------------------------------------------------

------------------------------ benchmark 'n1 = 1000, n2 = 1000000': 5 tests -----------------------------
Name (time in us)                                                      Mean              StdDev
---------------------------------------------------------------------------------------------------------
test_random[1000000-1000-linear_search_rust_noboundscheck]         868.1418 (1.0)       74.8734 (1.06)
test_random[1000000-1000-linear_search_numba]                    1,361.3032 (1.57)     105.9985 (1.50)
test_random[1000000-1000-linear_search_cython]                   2,012.2270 (2.32)      70.8773 (1.0)
test_random[1000000-1000-np_searchsorted]                       59,703.6301 (68.77)    309.4617 (4.37)
test_random[1000000-1000-linear_search_pure]                   143,736.0657 (165.57)   848.2648 (11.97)
---------------------------------------------------------------------------------------------------------

--------------------------- benchmark 'n1 = 1000000, n2 = 0': 5 tests ----------------------------
Name (time in ns)                                               Mean              StdDev
--------------------------------------------------------------------------------------------------
test_random[0-1000000-linear_search_rust_noboundscheck]     343.1752 (1.0)      182.6622 (4.69)
test_random[0-1000000-linear_search_numba]                  399.7146 (1.16)     223.1381 (5.73)
test_random[0-1000000-np_searchsorted]                      526.4312 (1.53)      52.6773 (1.35)
test_random[0-1000000-linear_search_pure]                   605.4443 (1.76)      38.9137 (1.0)
test_random[0-1000000-linear_search_cython]                 818.7875 (2.39)     264.7867 (6.80)
--------------------------------------------------------------------------------------------------

--------------------------------- benchmark 'n1 = 1000000, n2 = 1': 5 tests ----------------------------------
Name (time in ns)                                                       Mean                  StdDev
--------------------------------------------------------------------------------------------------------------
test_random[1-1000000-np_searchsorted]                              635.4328 (1.0)           48.9943 (1.0)
test_random[1-1000000-linear_search_rust_noboundscheck]         491,383.6285 (773.31)    13,564.8762 (276.87)
test_random[1-1000000-linear_search_numba]                      613,702.3999 (965.80)    77,155.0027 (>1000.0)
test_random[1-1000000-linear_search_cython]                   3,191,825.2086 (>1000.0)   29,114.8299 (594.25)
test_random[1-1000000-linear_search_pure]                   107,599,883.5848 (>1000.0)  405,733.7120 (>1000.0)
--------------------------------------------------------------------------------------------------------------

------------------------------ benchmark 'n1 = 1000000, n2 = 1000': 5 tests -----------------------------
Name (time in us)                                                      Mean              StdDev
---------------------------------------------------------------------------------------------------------
test_random[1000-1000000-np_searchsorted]                          188.8775 (1.0)        9.2289 (1.0)
test_random[1000-1000000-linear_search_rust_noboundscheck]         590.7254 (3.13)      10.4048 (1.13)
test_random[1000-1000000-linear_search_numba]                      816.5589 (4.32)      84.5074 (9.16)
test_random[1000-1000000-linear_search_cython]                   3,828.4083 (20.27)     41.0707 (4.45)
test_random[1000-1000000-linear_search_pure]                   144,789.2441 (766.58)   972.6912 (105.40)
---------------------------------------------------------------------------------------------------------

-------------------------- benchmark 'n1 = 1000000, n2 = 1000000': 5 tests ---------------------------
Name (time in ms)                                                     Mean            StdDev
------------------------------------------------------------------------------------------------------
test_random[1000000-1000000-linear_search_rust_noboundscheck]       9.1368 (1.0)      0.1166 (1.17)
test_random[1000000-1000000-linear_search_numba]                   10.4603 (1.14)     0.3167 (3.19)
test_random[1000000-1000000-linear_search_cython]                  13.7457 (1.50)     0.0993 (1.0)
test_random[1000000-1000000-np_searchsorted]                      123.1651 (13.48)    0.3161 (3.18)
test_random[1000000-1000000-linear_search_pure]                   306.1097 (33.50)    0.7911 (7.96)
------------------------------------------------------------------------------------------------------
```
