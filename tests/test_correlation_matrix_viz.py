from fast_eda.fast_eda import correlation_matrix_viz
import pandas as pd
import altair as alt


def test_empty_dataframe():
    """Test the function with an empty DataFrame."""
    df_empty = pd.DataFrame()
    chart = correlation_matrix_viz(df_empty)
    assert chart is not None, "Empty DataFrame test failed: No chart returned."
    assert isinstance(chart, alt.Chart), "Empty DataFrame test failed: Incorrect return type."
    assert len(chart.data) == 0, "Empty DataFrame test failed: Chart should have no data."



def test_no_numeric_columns():
    """Test the function with a DataFrame that has no numeric columns."""
    df_no_numeric = pd.DataFrame({
        "A": ["apple", "banana", "cherry"],
        "B": ["dog", "cat", "mouse"]
    })
    chart = correlation_matrix_viz(df_no_numeric)
    assert isinstance(chart, alt.Chart), "No numeric columns test failed."



def test_single_numeric_column():
    """Test the function with a DataFrame that has a single numeric column."""
    df_single_numeric = pd.DataFrame({
        "A": [1, 2, 3, 4, 5]
    })
    chart = correlation_matrix_viz(df_single_numeric)
    assert isinstance(chart, alt.Chart), "Single numeric column test failed."


def test_identical_numeric_columns():
    """Test the function with a DataFrame that has identical numeric columns."""
    df_identical_numeric = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": [1, 2, 3, 4, 5]
    })
    chart = correlation_matrix_viz(df_identical_numeric)
    assert isinstance(chart, alt.Chart), "Identical numeric columns test failed."


def test_diverse_numeric_columns():
    """Test the function with a DataFrame that has diverse numeric columns."""
    df_diverse_numeric = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": [2, 4, 6, 8, 10],
        "C": [5, 4, 3, 2, 1]
    })
    chart = correlation_matrix_viz(df_diverse_numeric)
    assert isinstance(chart, alt.Chart), "Diverse numeric columns test failed."

