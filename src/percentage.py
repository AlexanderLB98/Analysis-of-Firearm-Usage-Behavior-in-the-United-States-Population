import pandas as pd


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates relative values for permits, long guns, and handguns as a percentage of the total population.

    Args:
        df (pd.DataFrame): The DataFrame containing aggregated data by state and population information.

    Returns:
        pd.DataFrame: The DataFrame with three new columns 'permit_perc', 'longgun_perc', and 'handgun_perc'
                    containing the relative values.

    Example:
        df_relative = calculate_relative_values(df_merged)
    """
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['longgun'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
    

    print("First five rows of the DataFrame with relative values:")
    print(df.head(5))
    
    return df

def merge_datasets(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Merges the given datasets by state and prints the first five rows of the resulting DataFrame.

    Args:
        df_1 (pd.DataFrame): The DataFrame with aggregated data by state.
        df_2 (pd.DataFrame): The DataFrame with state population data.

    Returns:
        pd.DataFrame: The merged DataFrame containing information from both datasets.

    Example:
        df_merged = merge_datasets(df_data, df_population)
    """
    
    df = df1.merge(df2, on="state")
    
    print(df.head(5))
    
    return df