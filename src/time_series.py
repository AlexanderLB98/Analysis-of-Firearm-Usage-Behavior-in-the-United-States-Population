import pandas as pd
#import matplotlib
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

def time_evolution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a time series plot showing the evolution of 'permit', 'handgun', 
    and 'long_gun' numbers over the years.


    Args:
        df (pd.DataFrame): The DataFrame containing columns 'year', 'permit', 
        'handgun', and 'long_gun'.

    Returns:
        None

    Example:
        time_evolution(df)
    """

    
    df = df.groupby("year").sum().reset_index()

    fig = plt.figure()  
    plt.ion()
    plt.plot(df["year"], df["permit"], label=f"Permit")
    plt.plot(df["year"], df["longgun"], label=f"Long_gun")
    plt.plot(df["year"], df["handgun"], label=f"Hand_gun")

    plt.xlabel("Year")
    plt.title("Permits, hand_guns and long_guns per year")
    plt.xticks(rotation=45)
    plt.legend()

    plt.show(block=True)
    