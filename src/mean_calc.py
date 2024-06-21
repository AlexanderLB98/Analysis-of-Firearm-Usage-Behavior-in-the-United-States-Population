import pandas as pd
import matplotlib.pyplot as plt

def calc_mean(df: pd.DataFrame, plot=True) -> pd.DataFrame:
    
    if plot:
        print(f'The mean percentege for permit is: {round(df["permit_perc"].mean(), 2)}%')
        plt.figure()
        plt.plot(df["state"], df["permit_perc"])
        plt.xticks(rotation=45)
        plt.show(block=True)
        print("But Kentucky is and outlier and is messing the mean")    
    
    
    df_noKentucky = df[df["state"] != "Kentucky"]
    new_mean = df["permit_perc"].mean()

    df.loc[df["state"] == "Kentucky", "permit_perc"] = new_mean
    
    print(f'The fixed mean percentege for permit is: {round(df["permit_perc"].mean(), 2)}%')
    
    print("The mean is now much lower because we have normalized the value for Kentucky")