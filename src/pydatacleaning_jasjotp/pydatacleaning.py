import pandas as pd 
from typing import Optional, List, Any

def pivot_wider(df, cols: str | List[str], index: str | List[str], vals: str | List[str]) -> pd.DataFrame:
    """
    Pivot a pandas dataframe from long to wide format using df,pivot()

    Parameters
    ----------
    df : pandas DataFrame
        DataFrame to convert from long to wide format 
    cols : str or List of strs
        Column to use to make the new DataFrame's columns 
    index : str or List of strs
        Column to use to make the new DataFrame's index
    vals: str or List of strs
        Column(s) to use to populate the new column's values
    Returns
    -------
    pandas DataFrame
        The wide format of the long DataFrame.

    Examples
    --------
    >>> pivot_wider(df, 'test', 'id', 'result')
    8
    >>> pivot_wider(
            df,
            cols=['year', 'metric'],
            index=['country', 'region'],
            values=['value', 'value_scaled']
        )
    """
    return df.pivot(
        columns = cols,
        index = index,
        values = vals
    )

def pivot_longer(df, ind_vars: str | List[str], value_vars: str | List[str], var_name: str, value_name: str) -> pd.DataFrame:
    """
    Pivot a pandas dataframe from wide to long format using df.melt()

    Parameters
    ----------
    df : pandas DataFrame
        DataFrame to convert from wide to long format 
    ind_vars : str or List of strs
        Column(s) to use as the index/identifier columns of the new DataFrame
    value_vars : str or List of strs
        Column(s) to unpivot into values of the new column
    var_name: str
        Name to use for the new column that will store the variables
    value_name: str 
        Name to use for the new column that will store the values
    Returns
    -------
    pandas DataFrame
        The long format of the wide DataFrame.

    Examples
    --------
    >>> df = pd.DataFrame({
            "id": [1, 2],
            "A": [10, 30],
            "B": [20, 40],
         })
    >>> pivot_longer(
            df,
            ind_vars="id",
            value_vars=["A", "B"],
            var_name="test",
            value_name="result"
        )

       id test  result
    0   1    A      10
    1   2    A      30
    2   1    B      20
    3   2    B      40
    """
    return pd.melt(
        df,
        id_vars = ind_vars,
        value_vars = value_vars,
        var_name = var_name,
        value_name = value_name
    )
