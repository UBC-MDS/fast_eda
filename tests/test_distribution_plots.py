import pytest
import pandas as pd
from matplotlib.figure import Figure
from fast_eda.fast_eda import distribution_plots

# Test 1: Ensure the function returns a Matplotlib Figure and Axes array
def test_distribution_plots_returns_figure_and_axes():
    """
    Test that distribution_plots returns a Matplotlib Figure and correctly shaped Axes array.
    """
    df = pd.DataFrame({
        'numeric_col': [1, 2, 3, 4, 5],
        'string_col': ['a', 'b', 'a', 'c', 'b']
    })
    fig, axes = distribution_plots(df, c=2, r=1)
    assert isinstance(fig, Figure), "The returned figure is not a Matplotlib Figure object."
    assert axes.shape == (1, 2), "The axes array shape is incorrect."

# Test 2: Check if the function handles an empty DataFrame
def test_distribution_plots_empty_dataframe():
    """
    Test that distribution_plots raises an error when given an empty DataFrame.
    """
    df = pd.DataFrame()
    with pytest.raises(AssertionError, match="df is an empty DataFrame"):
        distribution_plots(df, c=2, r=1)

# Test 3: Check if the function raises an error for invalid column override
def test_distribution_plots_invalid_col_ovr():
    """
    Test that distribution_plots raises an error when col_ovr contains non-existent columns.
    """
    df = pd.DataFrame({
        'numeric_col': [1, 2, 3, 4, 5],
        'string_col': ['a', 'b', 'a', 'c', 'b']
    })
    with pytest.raises(AssertionError, match="some columns are not in df"):
        distribution_plots(df, c=2, r=1, col_ovr=['non_existent_col'])

# Test 4: Check if the function handles non-integer values for rows and columns
def test_distribution_plots_non_integer_rows_cols():
    """
    Test that distribution_plots raises an error when rows or columns are not integers.
    """
    df = pd.DataFrame({
        'numeric_col': [1, 2, 3, 4, 5]
    })
    with pytest.raises(AssertionError, match="c is not an integer"):
        distribution_plots(df, c='two', r=1)
    with pytest.raises(AssertionError, match="r is not an integer"):
        distribution_plots(df, c=2, r='one')

# Test 5: Check if the function raises an error for an invalid figsize
def test_distribution_plots_invalid_figsize():
    """
    Test that distribution_plots raises an error when figsize is not a tuple of two integers.
    """
    df = pd.DataFrame({
        'numeric_col': [1, 2, 3, 4, 5]
    })
    with pytest.raises(AssertionError, match="figsize is not a tuple of 2 integers"):
        distribution_plots(df, c=2, r=1, figsize=(10,))
    with pytest.raises(AssertionError, match="figsize is not a tuple of 2 integers"):
        distribution_plots(df, c=2, r=1, figsize=('10', 6))

# Test 6: Check if the function handles a DataFrame with only numeric columns
def test_distribution_plots_numeric_only():
    """
    Test that distribution_plots correctly handles a DataFrame with only numeric columns.
    """
    df = pd.DataFrame({
        'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50]
    })
    fig, axes = distribution_plots(df, c=1, r=2)
    assert isinstance(fig, Figure), "The returned figure is not a Matplotlib Figure object."
    assert axes.shape == (2,1), "The axes array shape is incorrect."

# Test 7: Check if the function handles a DataFrame with only string columns
def test_distribution_plots_string_only():
    """
    Test that distribution_plots correctly handles a DataFrame with only string columns.
    """
    df = pd.DataFrame({
        'col1': ['a', 'b', 'c', 'd', 'e'],
        'col2': ['x', 'y', 'z', 'w', 'v']
    })
    fig, axes = distribution_plots(df, c=1, r=2)
    assert isinstance(fig, Figure), "The returned figure is not a Matplotlib Figure object."
    assert axes.shape == (2,1), "The axes array shape is incorrect."

# Test 8: Check if the function hides unused axes correctly
def test_distribution_plots_unused_axes():
    """
    Test that distribution_plots hides unused Axes when more subplots are allocated than needed.
    """
    df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': [4, 5, 6]
    })
    fig, axes = distribution_plots(df, c=2, r=2)
    for ax in axes.flatten()[2:]:
        assert not ax.get_visible(), "Unused axes should be hidden."

# Test 9: Check if the function handles an edge case with a single column
def test_distribution_plots_single_column():
    """
    Test that distribution_plots correctly handles a DataFrame with a single numeric column.
    """
    df = pd.DataFrame({
        'col1': [1, 2, 3, 4, 5]
    })
    fig, axes = distribution_plots(df, c=1, r=1)
    assert isinstance(fig, Figure), "The returned figure is not a Matplotlib Figure object."
    assert axes.shape == (1,1), "The axes array shape is incorrect for a single plot."

# Test 10: Check if the function raises an error for invalid DataFrame type
def test_distribution_plots_invalid_dataframe():
    """
    Test that distribution_plots raises an error when given a non-DataFrame input.
    """
    with pytest.raises(AssertionError, match="df is not a pd.DataFrame"):
        distribution_plots([1, 2, 3], c=2, r=1)

# Test 11: Check if the function handles a non-numeric figsize
def test_distribution_plots_non_numeric_figsize():
    """
    Test that distribution_plots raises an error when figsize contains non-integer values.
    """
    df = pd.DataFrame({
        'numeric_col': [1, 2, 3, 4, 5]
    })
    with pytest.raises(AssertionError, match="figsize is not a tuple of 2 integers"):
        distribution_plots(df, c=2, r=1, figsize=(10.5, 6.5))

# Test 12: Check if the function handles DataFrame with duplicate columns
def test_distribution_plots_duplicate_columns():
    """
    Test that distribution_plots correctly processes a DataFrame with duplicate column names.
    """
    df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col1': [4, 5, 6]
    })
    fig, axes = distribution_plots(df, c=1, r=1)
    assert isinstance(fig, Figure), "The returned figure is not a Matplotlib Figure object."

# Test 13: Check if the function handles col_ovr being None
def test_distribution_plots_col_ovr_none():
    """
    Test that distribution_plots correctly handles col_ovr=None without errors.
    """
    df = pd.DataFrame({
        'numeric_col': [1, 2, 3, 4, 5],
        'string_col': ['a', 'b', 'a', 'c', 'b']
    })
    fig, axes = distribution_plots(df, c=2, r=1, col_ovr=None)
    assert isinstance(fig, Figure), "The returned figure is not a Matplotlib Figure object."
    assert axes.shape == (1, 2), "The axes array shape is incorrect."
