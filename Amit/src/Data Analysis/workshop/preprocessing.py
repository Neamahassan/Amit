import pandas as pd


def drop_cols(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Drop specific columns from a DataFrame.
    """
    return df.drop(columns=cols, errors='ignore')