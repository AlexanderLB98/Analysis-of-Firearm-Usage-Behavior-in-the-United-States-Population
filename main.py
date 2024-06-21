from src.common import read_csv, clean_csv,rename_col, clean_states
from src.dates import breakdown_date, erase_month
from src.grouping import groupby_state_and_year, groupby_state, print_biggest_handguns, print_biggest_longguns
from src.time_series import time_evolution
from src.percentage import merge_datasets
from src.percentage import calculate_relative_values
from src.mean_calc import calc_mean
from src.maps.plot_all_maps import main_maps
import os


if __name__ == "__main__":
    
    plot = True    

    url = os.path.join("data", "nics-firearm-background-checks.csv")
    
    # Reads csv into a pandas dataframe
    df = read_csv(url) 
    
    # Get only certain columns from the dataframe
    df = clean_csv(df)
    
    # Rename longgun to long_gun
    df = rename_col(df)
    
    # separate date into year and month
    df = breakdown_date(df)
    
    # Delete de month column
    df = erase_month(df)
    
    # Group the data by state and year
    df_grouped = groupby_state_and_year(df)
    
    # Most petitions for handguns and longguns
    print_biggest_handguns(df_grouped)
    print_biggest_longguns(df_grouped)
    
    # Time evolution
    if plot:
        time_evolution(df)
    
    
    conclussion = '''
    There is a clear upward trend with 
    a peak in 2017. The 3 variables are positively correlated, 
    as they have a similar evolution. The 2020 data are very 
    low because there is only information up to March, 
    so there is no information on the pandemic. It is 
    expected that the trend will continue to rise.\n
    '''
    print(conclussion)
    
    # Group by state
    df = groupby_state(df)
    
    # Remove states
    df = clean_states(df)
    
    # Merge datasets
    pop_url = os.path.join('data', 'us-state-populations.csv') 
    df_population = read_csv(pop_url)
    df = merge_datasets(df, df_population)
    
    # Calculate percentage
    df = calculate_relative_values(df)
    
    
    # Calculate means
    calc_mean(df, plot=plot)

    # Maps
    main_maps(df)