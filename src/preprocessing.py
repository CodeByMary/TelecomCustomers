import pandas as pd
from sklearn.preprocessing import LabelEncoder

def target_variable_distribution(df, target_col: str):
    """
    This function calculates and displays the distribution of the target variable in terms of count and percentage.

    Parameters:
        df (DataFrame): The input DataFrame (Pandas DataFrame).
        target_col (str): The name of the target column in the DataFrame.

    Returns:
        DataFrame: A DataFrame containing the distribution of the target variable.
    """
    # Calculate total number of rows in the dataset
    total_count = len(df)

    # Group by the target column and count the occurrences
    distribution_df = df[target_col].value_counts().reset_index()

    # Rename columns for clarity
    distribution_df.columns = [target_col, 'count']

    # Calculate the percentage of each class and add it as a new column
    distribution_df['percentage'] = round((distribution_df['count'] / total_count) * 100, 2)

    # Display the distribution with count and percentage
    print(f"Distribution of target variable '{target_col}':")
    print(distribution_df)

    return distribution_df


def encode_binary_columns(df):
    """
    This function encodes binary categorical columns (with exactly 2 unique values) in the DataFrame using Label Encoding.

    Parameters:
        df (DataFrame): The input DataFrame (Pandas DataFrame).

    Returns:
        DataFrame: The DataFrame with binary columns encoded.
    """
    # Initialize label encoder
    le = LabelEncoder()

    # Iterate through each column to detect binary columns
    for col_name in df.columns:
        unique_values = len(df[col_name].unique())

        # Check if the column is binary (exactly 2 unique values)
        if unique_values == 2:
            # Apply Label Encoding (0, 1) to binary columns
            df[col_name] = le.fit_transform(df[col_name])
            print(f"Encoded binary column: {col_name}")

    return df



def encode_non_binary_columns(df):
    """
    This function encodes non-binary categorical columns (with more than 2 unique values) using One-Hot Encoding.
    Numeric columns (int and float types) and binary columns are skipped.

    Parameters:
        df (DataFrame): The input DataFrame (Pandas DataFrame).

    Returns:
        DataFrame: The original DataFrame with non-binary columns encoded.
    """
    # Iterate through each column to detect non-binary categorical columns
    for col_name in df.columns:
        # Skip numeric columns (int, float)
        if pd.api.types.is_numeric_dtype(df[col_name]):
            continue
        
        unique_values = len(df[col_name].unique())

        # Skip binary columns (columns with exactly 2 unique values)
        if unique_values == 2:
            continue

        # Apply One-Hot Encoding for columns with more than 2 unique values and of type 'object'
        if unique_values > 2 and df[col_name].dtype == 'object':
            # Use pandas get_dummies for One-Hot Encoding
            df = pd.get_dummies(df, columns=[col_name], prefix=[col_name])
            print(f"One-hot encoded column: {col_name}")

    return df



def check_column_numeric(df, column_name):
    """
    Checks if a specified column contains any non-numeric values, and returns 
    the DataFrame of problematic rows where the column cannot be converted to numeric.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the column to check.

    Returns:
        pd.DataFrame: A DataFrame with problematic rows for the specified column.
    """
    if column_name in df.columns and df[column_name].dtype == 'object':
        # Convert the column to numeric, setting errors='coerce' will turn non-numeric values into NaN
        problematic_rows = df[pd.to_numeric(df[column_name], errors='coerce').isna() & (df[column_name] != '')]
        return problematic_rows
    else:
        return pd.DataFrame()  # Return an empty DataFrame if the column is numeric or doesn't exist



def clean_column_names(df):
    """
    Clean the column names of the DataFrame by converting to lowercase,
    replacing spaces with underscores, and removing any brackets or special characters.
    
    Parameters:
    df (pd.DataFrame): The DataFrame whose column names need to be cleaned.
    
    Returns:
    pd.DataFrame: The DataFrame with cleaned column names.
    """
    # Convert to lowercase
    df.columns = df.columns.str.lower()
    
    # Replace spaces with underscores
    df.columns = df.columns.str.replace(' ', '_', regex=False)
    
    # Remove special characters like brackets and parentheses
    df.columns = df.columns.str.replace(r'[(){}\[\]]', '', regex=True)
    
    return df

