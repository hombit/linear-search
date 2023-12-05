use numpy::PyArray1;
use pyo3::prelude::*;

/// Find the place index of each element of b in a. Both a and b are sorted.
#[pyfunction(name = "linear_search_rust")]
fn linear_search<'py>(
    py: Python<'py>,
    a: &'py PyArray1<f64>,
    b: &'py PyArray1<f64>,
) -> &'py PyArray1<usize> {
    let a = a.readonly();
    let a = a.as_array();
    let b = b.readonly();
    let b = b.as_array();

    let mut idx = vec![a.len(); b.len()];

    if a.is_empty() || b.is_empty() {
        return PyArray1::from_vec(py, idx);
    }

    let mut i = 0;
    let mut j = 0;

    while i < a.len() && j < b.len() {
        while j < b.len() && b[j] < a[i] {
            idx[j] = i;
            j += 1;
        }
        i += 1;
    }

    PyArray1::from_vec(py, idx)
}

#[pyfunction(name = "linear_search_rust_noboundscheck")]
fn linear_search_noboundscheck<'py>(
    py: Python<'py>,
    a: &'py PyArray1<f64>,
    b: &'py PyArray1<f64>,
) -> &'py PyArray1<usize> {
    let a = a.readonly();
    let a = a.as_array();
    let b = b.readonly();
    let b = b.as_array();

    let mut idx = vec![a.len(); b.len()];

    if a.is_empty() || b.is_empty() {
        return PyArray1::from_vec(py, idx);
    }

    let mut i = 0;
    let mut j = 0;

    while i < a.len() && j < b.len() {
        while j < b.len() && unsafe { b.uget(j) } < unsafe { a.uget(i) } {
            *unsafe { idx.get_unchecked_mut(j) } = i;
            j += 1;
        }
        i += 1;
    }

    PyArray1::from_vec(py, idx)
}

/// A Python module implemented in Rust.
#[pymodule]
fn linear_search_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(linear_search, m)?)?;
    m.add_function(wrap_pyfunction!(linear_search_noboundscheck, m)?)?;
    Ok(())
}
