import math


def give_bmi(
            height: list[int | float],
            weight: list[int | float]) -> list[int | float]:
    """ Calculating the body mass index. """
    li = []
    try:
        assert len(height) == len(weight), \
            "Lists are not same size."
        for i in range(len(height)):
            assert height[i] > 0 and weight[i] > 0, \
                "Height or Weight can not be zero."
            assert isinstance(weight[i], (int, float)) and \
                isinstance(height[i], (int, float)), \
                "Instances can be int or float."
            li.append(float(weight[i] / math.pow(height[i], 2)))
    except AssertionError as e:
        print(e)
        exit(1)
    return li


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ checking the is list element above the limit """
    try:
        assert limit >= 0 and isinstance(limit, int), \
            "Limit need to be int and bigger than 0."
        for i in bmi:
            assert i > 0 and isinstance(i, (int, float)), \
                "Bmi instance need to be int and bigger than 0."
    except AssertionError as e:
        print(e)
        exit(1)
    return [lim > limit for lim in bmi]
