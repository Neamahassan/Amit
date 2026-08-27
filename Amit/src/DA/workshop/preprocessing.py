import pandas as pd


def drop_cols(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    return df.drop(columns=cols)


def get_data_summary(df):
    return pd.DataFrame({"Dtypes ": df.dtypes, "N_uniques ": df.nunique()}).T