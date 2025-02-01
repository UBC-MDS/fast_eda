import pytest
import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now import fast_eda
from fast_eda.fast_eda import describe_function


# Test if the median is a float
def test_median_is_float():
    """
    Test that the median value returned by describe_function is a float for all numeric columns.
    """
    # Define test DataFrames
    df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    df2 = pd.DataFrame({'A': [1.1, 2.2, 3.3, 4.4, 5.5], 'B': [11.1, 22.2, 33.3, 44.4, 55.5]})
    
    # Test first DataFrame
    stats1 = describe_function(df1)
    for column in stats1.columns:
        assert isinstance(stats1.loc['50%', column], float), f"Median of column {column} in df1 is not a float"
    
    # Test second DataFrame
    stats2 = describe_function(df2)
    for column in stats2.columns:
        assert isinstance(stats2.loc['50%', column], float), f"Median of column {column} in df2 is not a float"

# Test if the mean is a float
def test_mean_is_float():
    """
    Test that the mean value returned by describe_function is a float for all numeric columns.
    """
    # Define test DataFrames
    df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    df2 = pd.DataFrame({'A': [1.1, 2.2, 3.3, 4.4, 5.5], 'B': [11.0, 22.0, 33.0, 44.0, 55.0]})
    
    # Test first DataFrame
    stats1 = describe_function(df1)
    for column in stats1.columns:
        assert isinstance(stats1.loc['mean', column], float), f"Mean of column {column} in df1 is not a float"
    
    # Test second DataFrame
    stats2 = describe_function(df2)
    for column in stats2.columns:
        assert isinstance(stats2.loc['mean', column], float), f"Mean of column {column} in df2 is not a float"

# Test if the standard deviation is greater than 0
def test_stdv_is_greater_than_zero():
    """
    Test that the standard deviation returned by describe_function is greater than zero for all numeric columns.
    """
    # Define test DataFrames
    df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    df2 = pd.DataFrame({'A': [1.0, 2.0, 3.0, 4.0, 5.0], 'B': [10.0, 20.0, 30.0, 40.0, 50.0]})
    
    # Test first DataFrame
    stats1 = describe_function(df1)
    for column in stats1.columns:
        stdv_value = stats1.loc['std', column]
        assert stdv_value > 0, f"Standard deviation for column {column} in df1 is not greater than 0"
    
    # Test second DataFrame
    stats2 = describe_function(df2)
    for column in stats2.columns:
        stdv_value = stats2.loc['std', column]
        assert stdv_value > 0, f"Standard deviation for column {column} in df2 is not greater than 0"
