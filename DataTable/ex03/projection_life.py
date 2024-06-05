from load_csv import load
from pandas import DataFrame
import matplotlib.pyplot as plt


def convert_gdp(li: list):
    """  """
    return [(float(i[:-1]) * 1000 if i[-1] == 'k' else float(i)) for i in li]


def convert_le(li: list):
    """  """
    return [float(i) for i in li]


def show_graph(le: DataFrame, gdp: DataFrame) -> None:
    """
    Display a graph of population projections over time.
    Parameters:
    - LE (DataFrame): DataFrame containing life expectancy data.
    - GDP (DataFrame): DataFrame containing GDP data.
    """
    gdp = gdp['1900'].tolist()
    le = le['1900'].tolist()
    plt.scatter(gdp, le[:195])
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')
    plt.xscale('log')
    plt.show()


if __name__ == "__main__":
    show_graph(
        load("life_expectancy_years.csv"),
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
