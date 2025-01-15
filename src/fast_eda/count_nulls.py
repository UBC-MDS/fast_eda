import pandas as pd 

def counts(df):
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
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    return df.isnull().sum().astype('int64')