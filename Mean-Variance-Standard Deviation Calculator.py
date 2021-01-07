import numpy as np


def calculate(list):
    if len(list) == 9:
        array = np.array(list).reshape(3, 3)
        calculations = {
            "mean": [(array.mean(axis=0).tolist()), array.mean(axis=1).tolist(), array.mean().tolist()],
            "variance": [(array.var(axis=0).tolist()), (array.var(axis=1).tolist()), (array.var().tolist())],
            "standard deviation": [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std().tolist()],
            "max": [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max().tolist()],
            "min": [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min().tolist()],
            "sum": [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum().tolist()]

        }
#        for key, value in calculations.items():
#            print(key, ":", value)

    else:
        raise Exception("Oops!  That was no valid number.  Try again...")

    return calculations


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))