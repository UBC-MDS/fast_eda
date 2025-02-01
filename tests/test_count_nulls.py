import pytest 
import pandas as pd

from fast_eda.fast_eda import count_nulls

def test_count_standard():
    """
    Test count_nulls function with a standard DataFrame containing some missing values.
    
    Example:
    --------
    Input DataFrame:
        A    B
    0   1  NaN
    1   2    2
    2 NaN    3

    Expected output:
        A    1
        B    1
    (Counts of NaN values in each column)
    """
    df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 2, 3]})
    expected = pd.Series({'A': 1, 'B': 1})
    result = count_nulls(df)
    assert result.equals(expected)
    
def test_counts_no_missing():
    """
    Test count_nulls function with a DataFrame that contains no missing values.

    Example:
    --------
    Input DataFrame:
        A  B
    0   1  4
    1   2  5
    2   3  6

    Expected output:
        A    0
        B    0
    (No missing values in any column)
    """
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected = pd.Series({'A': 0, 'B': 0})
    result = count_nulls(df)
    assert result.equals(expected)   

def test_counts_all_missing():
    """
    Test count_nulls function with a DataFrame where all values are missing.

    Example:
    --------
    Input DataFrame:
        A    B
    0 NaN  NaN
    1 NaN  NaN

    Expected output:
        A    2
        B    2
    (Each column has 2 missing values)
    """
    df = pd.DataFrame({'A': [None, None], 'B': [None, None]})
    expected = pd.Series({'A': 2, 'B': 2})
    result = count_nulls(df)
    assert result.equals(expected)

def test_counts_empty_df():
    """
    Test count_nulls function with an empty DataFrame.

    Example:
    --------
    Input DataFrame:
        (empty DataFrame)

    Expected output:
        (empty Pandas Series with dtype 'int64')
    """
    df = pd.DataFrame()
    expected = pd.Series(dtype='int64')
    result = count_nulls(df)
    assert result.equals(expected)

def test_counts_invalid_input():
    """
    Test count_nulls function with an invalid input type (non-DataFrame).
    
    Example:
    --------
    Input:
        "not a DataFrame" (a string instead of a DataFrame)

    Expected behavior:
        A ValueError should be raised.
    """
    with pytest.raises(ValueError):
        count_nulls("not a DataFrame")
