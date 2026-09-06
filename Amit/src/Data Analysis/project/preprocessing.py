# preprocessing.py

import pandas as pd
import os


def read_data_file(file_path):
    """
    Read a CSV data file and return it as a Pandas DataFrame.

    Handles common errors such as an invalid file path,
    an empty file, or an invalid CSV format.

    Parameters
    ----------
    file_path : str
        The path to the CSV file.

    Returns
    -------
    pd.DataFrame or None
        The DataFrame if reading is successful,
        or None if an error occurs.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File not found at path: {file_path}"
            )

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Check if the DataFrame is empty
        if df.empty:
            print(
                f"Warning: The file '{file_path}' was read successfully "
                "but contains no data."
            )

        # Display a success message with the DataFrame dimensions
        print(
            f"Data loaded successfully from: {file_path} "
            f"| Shape: {df.shape}"
        )

        return df

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

    except pd.errors.EmptyDataError:
        print(
            f"Error: The file '{file_path}' is empty "
            "and contains no readable data."
        )
        return None

    except pd.errors.ParserError:
        print(
            f"Error: Failed to parse the file '{file_path}'. "
            "Make sure it is a valid CSV file."
        )
        return None

    except Exception as e:
        print(
            f"Unexpected error while reading the file: {e}"
        )
        return None


def drop_unnecessary_features(df, cols_to_drop):
    """
    Drop unnecessary columns from a DataFrame.

    The columns are provided as a list, usually from the
    configuration file, making the function reusable with
    different datasets.

    Parameters
    ----------
    df : pd.DataFrame
        The original DataFrame.

    cols_to_drop : list
        A list of column names to be removed.

    Returns
    -------
    pd.DataFrame or None
        A new DataFrame after removing the specified columns,
        or None if the input DataFrame is None.
    """
    # Check if the DataFrame exists
    if df is None:
        print("Error: No DataFrame available to drop columns from.")
        return None

    # Find columns that actually exist in the DataFrame
    existing_cols = [
        col for col in cols_to_drop
        if col in df.columns
    ]

    # Find columns that do not exist in the DataFrame
    missing_cols = [
        col for col in cols_to_drop
        if col not in df.columns
    ]

    # Display a warning for missing columns
    if missing_cols:
        print(
            f"Warning: The following columns do not exist "
            f"and will not be dropped: {missing_cols}"
        )

    # Drop the existing columns
    df_dropped = df.drop(columns=existing_cols)

    # Display information about the removed columns
    print(f"Dropped columns: {existing_cols}")

    # Display the number of columns after dropping
    print(
        f"Number of columns after dropping: "
        f"{df_dropped.shape[1]}"
    )

    return df_dropped


def check_data_type(df):
    """
    Create a small Data Quality Report for each column.

    The report includes:
    - Data type (Dtype)
    - Number of non-null values
    - Number of missing values
    - Number of unique values

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to inspect.

    Returns
    -------
    pd.DataFrame or None
        A transposed Data Quality Report,
        or None if the input DataFrame is None.
    """
    # Check if the DataFrame exists
    if df is None:
        print("Error: No DataFrame available to inspect.")
        return None

    # Create the Data Quality Report
    report = pd.DataFrame({
        "Dtype": df.dtypes,
        "Non-Null Count": df.notnull().sum(),
        "Missing Values": df.isnull().sum(),
        "Unique Values (nunique)": df.nunique()
    })

    # Transpose the report to make it easier to read
    report_transposed = report.T

    return report_transposed