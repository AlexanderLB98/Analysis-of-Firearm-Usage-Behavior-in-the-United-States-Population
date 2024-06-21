import pandas as pd

def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs a cumulative total calculation grouped by year and state on the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing columns 'year' and 'state' for grouping.

    Returns:
        pd.DataFrame: The DataFrame with cumulative totals aggregated by year and state.

    Example:
        df_grouped = groupby_state_and_year(df)
    """

    
    df = df.groupby(["year", "state"]).sum().reset_index()
    
    print("Grouped data: ")
    print(df.head(5))
    
    
    return df

def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Groups the DataFrame by state to show total values, ignoring the grouping by year.

    Args:
        df (pd.DataFrame): The DataFrame containing cumulative totals aggregated by year and state.

    Returns:
        pd.DataFrame: The DataFrame with cumulative totals aggregated only by state.

    Example:
        df_grouped_by_state = groupby_state(df_grouped_by_state_year)
    """

    # Group by state and calculate total values
    df_grouped = df.groupby('state').sum().reset_index().drop(columns="year")
    
    print("Group only by state")
    print(df_grouped.head(5))
    
    return df_grouped



def print_biggest_handguns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prints the state and year with the highest number of handguns from the grouped DataFrame.
    
    Args:
        df (pd.DataFrame): The grouped DataFrame containing cumulative totals aggregated by 
        year and state.

    Returns:
        None

    Example:
        print_biggest_handguns(df)
    """
    
    index = df["handgun"].idxmax()
    
    state = df.iloc[index]["state"]
    year = df.iloc[index]["year"]
    handgun = df.iloc[index]["handgun"]
    
    print(f"{state} was the state with more petitions for handguns "
      f"in the year {str(year)}, with {str(int(handgun))} petitions")


def print_biggest_longguns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prints the state and year with the highest number of long guns from the grouped DataFrame.

    Args:
        df (pd.DataFrame): The grouped DataFrame containing cumulative totals aggregated by year and state.

    Returns:
        None

    Example:
    print_biggest_longguns(df)

    """
        
    index = df["longgun"].idxmax()
    
    state = df.iloc[index]["state"]
    year = df.iloc[index]["year"]
    longgun = df.iloc[index]["longgun"]
    
    print(f"{state} was the state with more petitions for handguns "
      f"in the year {str(year)}, with {str(int(longgun))} petitions")
