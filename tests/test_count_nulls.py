import pytest 
import pandas as pd

from fast_eda.count_nulls import counts

def test_count_standard():

    df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 2, 3]})
    expected = pd.Series({'A': 1, 'B': 1})
    result = counts(df)
    assert result.equals(expected)
    
def test_counts_no_missing():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected = pd.Series({'A': 0, 'B': 0})
    result = counts(df)
    assert result.equals(expected)   

def test_counts_all_missing():
    df = pd.DataFrame({'A': [None, None], 'B': [None, None]})
    expected = pd.Series({'A': 2, 'B': 2})
    result = counts(df)
    assert result.equals(expected)

def test_counts_empty_df():
    df = pd.DataFrame()
    expected = pd.Series(dtype='int64')
    result = counts(df)
    assert result.equals(expected)

def test_counts_invalid_input():
    with pytest.raises(ValueError):
        counts("not a DataFrame")