import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    try:
        open(path, 'r')
        assert path.endswith('.csv'), f"File extension is not .csv: {path}"
        csv = pd.read_csv(path, index_col=0)
        print(f"Loading dataset of dimensions {csv.shape}")
        return csv
    except FileNotFoundError:
        print(f"File not found: {path}")
        exit(1)
    except AssertionError as e:
        print(f" {e}")
        exit(1)
    except pd.errors.ParserError:
        print("Error parsing file")
        exit(1)
    except pd.errors.EmptyDataError:
        print("Data is empty")
        exit(1)
