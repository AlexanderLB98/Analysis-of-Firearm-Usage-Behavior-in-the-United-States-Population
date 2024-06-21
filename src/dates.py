import pandas as pd



def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes the 'month' column from the given DataFrame and prints the first five rows and column names.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the 'month' column to be removed.

    Returns:
        pd.DataFrame: The DataFrame without the 'month' column.

    Example:
        df = erase_month(df)
    """

    if "month" in df.columns:
        print("Deleting month column")
        df.drop(columns=["month"],inplace=True)
    else:
        print("No columne called month")
    
    print(df.head(5))
    print(df.columns)
    
    return df

def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Breaks down the 'month' column into 'year' and 'month' columns in the given DataFrame 
    and prints the first five rows.

    Args:
        df (pd.DataFrame): The DataFrame containing the 'month' column with date information as str.

    Returns:
        pd.DataFrame: The DataFrame with the 'month' column split into 'year' and 'month' columns.


    Example:
        df = breakdown_date(df)
    """


    
    # Apply the format_date function to split the 'month' column
    df[['year', 'month']] = pd.DataFrame(df['month'].map(format_date).tolist())    
   
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