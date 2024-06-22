import pandas as pd



def erase_month(df: pd.DataFrame, test_mode: bool = False) -> pd.DataFrame:
    """
    Removes the 'month' column from the given DataFrame and prints the first five rows and column names.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the 'month' column to be removed.
        test_mode (bool): If True, suppresses print statements. Default is False.

    Returns:
        pd.DataFrame: The DataFrame without the 'month' column.

    Example:
        df = erase_month(df)
    """

    if "month" in df.columns:
        if not test_mode:
            print("Deleting month column")
        df.drop(columns=["month"],inplace=True)
    else:
        if not test_mode:
            print("No columne called month")
    
    
    if not test_mode:
        print(df.head(5))
        print(df.columns)
    
    return df

def breakdown_date(df: pd.DataFrame,test_mode: bool = False) -> pd.DataFrame:
    """
    Breaks down the 'month' column into 'year' and 'month' columns in the given DataFrame 
    and prints the first five rows.

    Args:
        df (pd.DataFrame): The DataFrame containing the 'month' column with date information as str.
        test_mode (bool): If True, suppresses print statements. Default is False.

    Returns:
        pd.DataFrame: The DataFrame with the 'month' column split into 'year' and 'month' columns.


    Example:
        df = breakdown_date(df)
    """

    
    # Apply the format_date function to split the 'month' column
    df[['year', 'month']] = pd.DataFrame(df['month'].map(format_date).tolist())    
   
    # Convert 'year' and 'month' columns to int
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    
    if not test_mode:
        print(df.head(5))
    
    return df

def format_date(date: str) -> list:
    """
    Converts date in year-month format into a list with 2 components: year and month

    Args:
        date (str): date in formate "YYYY-MM"

    Returns:
        list: List with 2 string components: ["YYYY", "MM"]
        
    Example:
        
    """
        
    date_list = date.split("-")  
    
    return date_list