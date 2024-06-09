from load_csv import load
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def convert_gdp(li: list):
    """Converts a list of GDP values to numeric format.
    Args:
        li (list): A list of GDP values.
    Returns:
        list: A list of converted GDP values.
    Example:
        convert_gdp(['1.5k', '2.7M', '3.2B'])
        [1500.0, 2700000.0, 3200000000.0]
    """
    return [(float(i[:-1]) * 1000 if i[-1] == 'k' else float(i)) for i in li]


def convert_le(li: list):
    """Converts a list of numbers to a list of floats.
    Args:
        li (list): The input list of numbers.
    Returns:
        list: A new list containing the converted numbers as floats.
    """
    return [float(i) for i in li]


def myFormat(x, pos):
    """ Format y-axis labels. """
    if x >= 1e3:
        return f'{x*1e-3:.0f}K'
    else:
        return f'{x:.0f}'


def show_graph(le: DataFrame, gdp: DataFrame) -> None:
    """
    Display a graph of population projections over time.
    Parameters:
    - LE (DataFrame): DataFrame containing life expectancy data.
    - GDP (DataFrame): DataFrame containing GDP data.
    """
    # gdp = gdp['1900']
    # le = le['1900']
    print(le['1900'])
    plt.scatter(gdp['1900'], le['1900'])
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.xscale('log')
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(myFormat))
    plt.gca().set_xticks([300, 1000, 10000])
    plt.title('1900')
    plt.show()


if __name__ == "__main__":
    show_graph(
        load("life_expectancy_years.csv"),
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
