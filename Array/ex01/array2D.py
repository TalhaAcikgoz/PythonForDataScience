import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ Slice the list from start to end. """
    try:
        assert isinstance(family, list) and\
            isinstance(start, int) and isinstance(end, int), \
            "Argument type error."
        assert len(family) > start and len(family) > end and len(family) > 0, \
            "Start and end can not be bigger than size of Family."
        fam = np.array(family)
        print(f"My shape is : {fam.shape}")
        fam = fam[start:end]
        print(f"My new shape is : {fam.shape}")
        return fam.tolist()
    except ValueError as ve:
        print(ve)
        exit(1)
    except AssertionError as e:
        print(e)
        exit(1)
    return []
