import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

def describe_function(df):
    """
    Generate summary statistics for numeric columns in the DataFrame.

    This function computes basic statistics such as mean, median, 
    standard deviation, minimum, and maximum for each numeric column 
    in the DataFrame, providing an overview of the central tendency 
    and spread of the data.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame containing numeric columns.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the calculated summary statistics for 
        each numeric column.
    """
    pass

def distribution_plots(df, c, r,  figsize = (10,  6), col_ovr=None):
    """
    Plots distributions of columns from a DataFrame using Matplotlib subplots and Seaborn plots.

    This function creates a grid of subplots to visualize the distributions of specified columns from a DataFrame.
    Numeric columns are plotted using histograms, while string columns are plotted using bar plots.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data to be plotted. Must not be empty.

    c : int
        The number of columns in the subplot grid.

    r : int
        The number of rows in the subplot grid.

    figsize : tuple of int, optional, default=(10, 6)
        The size of the figure in inches (width, height).

    col_ovr : list of str, optional
        A list of column names to plot. If None, all columns in the DataFrame are used.
        Must be a subset of the DataFrame's columns.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The Matplotlib figure object containing the subplots.

    axes : numpy.ndarray of matplotlib.axes._subplots.AxesSubplot
        An array of Axes objects corresponding to the subplots.

    Raises
    ------
    AssertionError
        If input validation fails for any of the parameters.

    Notes
    -----
    - The function handles both numeric and string columns differently:
        - Numeric columns: Plotted using Seaborn's `histplot`.
        - String columns: Plotted using Seaborn's `barplot` without error bars.
    - Any unused subplot axes are hidden to prevent empty plots.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'numeric_col': [1, 2, 3, 4, 5],
    ...     'string_col': ['a', 'b', 'a', 'c', 'b']
    ... })
    >>> fig, axes = distribution_plotting_function(df, c=2, r=1)
    """

    # user inpute validation
    assert isinstance(df, pd.DataFrame), 'df is not a pd.DataFrame'
    assert len(df) > 0, 'df is an empty DataFrame'
    assert isinstance(c, int) and c > 0, 'c is not an integer > 0'
    assert isinstance(r, int) and r > 0, 'r is not an integer > 0'
    assert isinstance(figsize, tuple), 'figsize is not a tuple of 2 integers'
    if isinstance(figsize, tuple):
        assert len(figsize) == 2, 'figsize is not a tuple of 2 integers'
        assert all(isinstance(x, int) for x in figsize), 'figsize is not a tuple of 2 integers'
    if col_ovr:
        assert isinstance(col_ovr, list), 'col_ovr is not a list of string'
        assert all(isinstance(x, str) for x in col_ovr), 'col_ovr is not a list of string'
        assert set(col_ovr).issubset(set(df.columns.tolist())), 'some columns are not in df'

    columns = col_ovr if col_ovr else df.columns.tolist()
    d = len(columns)
    
    fig, axes = plt.subplots(
        nrows=r, ncols=c, figsize=figsize, sharex=False, sharey=False, squeeze=False
    )
    axes_flat = axes.flatten()
    for i, col in enumerate(columns):
        series = df[col]
        if is_numeric_dtype(series):
            sns.histplot(series, ax=axes_flat[i])
        elif is_string_dtype(series):
            sns.barplot(series, errorbar=None, ax=axes_flat[i])
     # hide unuse Axes objects
    if d < len(axes_flat):
        for ax in axes_flat[d:]:
            ax.set_visible(False)
    fig.tight_layout()
    return fig, axes

def counts_function(df):
    """
    Count missing values in each column of the DataFrame.

    This function returns the number of missing (NaN) values for each column 
    in the DataFrame, helping to identify which columns require data cleaning 
    or imputation.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame to be analyzed.

    Returns
    -------
    pandas.Series
        A Series with the number of missing values for each column.
    """
    pass

def correlation_matrix(df):
    """
    Generate a correlation matrix for numeric columns in the DataFrame.

    This function computes the Pearson correlation coefficients between 
    all numeric columns in the DataFrame, showing how strongly each 
    feature is related to the others.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame containing numeric columns.

    Returns
    -------
    pandas.DataFrame
        A DataFrame representing the correlation matrix between numeric 
        columns in the input DataFrame.
    """
    pass
