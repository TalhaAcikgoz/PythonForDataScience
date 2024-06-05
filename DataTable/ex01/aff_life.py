from load_csv import load
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt


def aff_life(csv: DataFrame) -> None:
    """ Plot life expectancy of Turkey over the years"""
    try:
        life_expectancy = csv.loc['Turkey']
        years = [int(i) for i in csv.columns][:len(life_expectancy)+1]
        plt.plot(list(years), life_expectancy)
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.title("Turkey Life Expectancy Projections")
        plt.show()
    except pd.errors.EmptyDataError:
        print("Data is empty")
    except KeyError:
        print("Country not found")


if __name__ == '__main__':
    aff_life(load("life_expectancy_years.csv"))
