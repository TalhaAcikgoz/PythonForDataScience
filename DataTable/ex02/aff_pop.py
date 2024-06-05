import matplotlib.pyplot as plt
from load_csv import load
from pandas import DataFrame
import matplotlib.ticker as ticker


def custom_format(x, pos):
    if x >= 1e6:
        return f'{x*1e-6:.1f}M'
    elif x >= 1e3:
        return f'{x*1e-3:.1f}K'
    else:
        return f'{x:.0f}'


def millions(nums: list) -> list:
    """ Convert a list of numbers to millions. """
    return [float(i[:-1]) * 1000 if i[-1] == 'k' else float(i[:-1]) * 1000000 for i in nums]


def aff_pop(csv: DataFrame) -> None:
    """ Plot population projections for Turkey and Italy. """
    try:
        turkey = csv.loc['Turkey']
        turkey = millions(turkey.tolist())
        population = [int(i) for i in csv.columns]
        plt.plot(population[:-50], list(turkey)[:-50], label='Turkey')
        italy = csv.loc['Italy']
        italy = millions(italy.tolist())
        population = [int(i) for i in csv.columns]
        plt.plot(population[:-50], list(italy)[:-50], label='Italy')
        formatter = ticker.FuncFormatter(custom_format)
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        plt.legend()
        plt.show()
    except KeyError:
        print("Country not found")


if __name__ == '__main__':
    aff_pop(load('population_total.csv'))
