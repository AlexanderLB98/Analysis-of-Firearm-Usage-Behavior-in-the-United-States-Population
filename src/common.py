import pandas as pd


def read_csv(url: str)-> pd.DataFrame: 
    """
    Reads a CSV file from the given URL and displays the first five rows and structure of the DataFrame.

    Args:
        url (str): The URL of the CSV file to be read.

    Returns:
        pd.DataFrame: The DataFrame containing the data read from the CSV file.

    Example:
        url = "data/nics-firearm-background-checks.csv"
        df = read_csv(url)
    """

    
    df = pd.read_csv(url)
    print(f'Columns: {df.columns.values}')
    print(df.head(5)) # Print 5 first rows
    print(df.info())  # print structure
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the dataset by retaining only the specified columns and prints the column names.


    Args:
        df (pd.DataFrame): The initial DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame containing only the specified columns.
    
    Raises:
        KeyError: If any of the specified columns are not found in the DataFrame.

    Example:
        clean_df = clean_csv(initial_df)
    """
    
    cols = ["month", "state", "permit", "handgun", "long_gun"]
    df_clean = df[cols].copy()
    
    
    
    # Convert specific columns to int
    df_clean["permit"] = pd.to_numeric(df_clean["permit"], errors='coerce').fillna(0).astype(int)
    df_clean["handgun"] = pd.to_numeric(df_clean["handgun"], errors='coerce').fillna(0).astype(int)
    df_clean["long_gun"] = pd.to_numeric(df_clean["long_gun"], errors='coerce').fillna(0).astype(int)
    
    
    print(df_clean.columns)
    
    return df_clean


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renames the 'longgun' column to 'long_gun' in the given DataFrame and prints the column names.

    This function takes a DataFrame as input, checks if the 'longgun' column exists, renames it to 'long_gun',
    prints the names of all the columns in the DataFrame after the renaming operation, and then returns the updated DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame with all its columns.

    Returns:
        pd.DataFrame: The DataFrame with the 'longgun' column renamed to 'long_gun'.

    Example:
        df = rename_col(df)        
    """

    if "long_gun" in df.columns:
        print("Renaming column name long_gun to longgun")
        df.rename(columns={"long_gun": "longgun"}, inplace=True)
    else:
        print("There is no column called long_gun")
    
    print(df.columns)
    return df


def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes specific states from the DataFrame and displays the number of unique states.

    Args:
        df (pd.DataFrame): The DataFrame grouped by state.

    Returns:
        pd.DataFrame: The DataFrame without the specified states.

    Example:
        df_cleaned = clean_states(df_grouped_by_state)
    """
    
    states_to_remove = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    
    states_present = df['state'].isin(states_to_remove)
    if states_present.any():
        print("Removing states from DataFrame:", df['state'][states_present].unique())
        df = df[~df['state'].isin(states_to_remove)]    
        
        print("Number of unique states remaining:", df['state'].nunique())

    return df
