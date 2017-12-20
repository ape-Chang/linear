#!/usr/bin/env python3

import numpy as np

# the linear model for [y = x*w + b + e] is predefined as
# w is [1 1 ... 1], b is 1, e is gaussian distributed noise.


def generate():
    """ generate a sample data set.

    :return: a stream of sample chunks. each chunk consist of 1024 samples
    """
    for i in range(1024):
        yield load()


def load():
    """ generate a sample data set.

    :return: a sample set of 1024 samples
    """
    samples = [None] * 1024
    for i in range(1024):
        x = np.random.rand(49) * 10 + 1
        y = np.sum(x) + np.random.rand()
        samples[i] = (x, y)
    return samples


if __name__ == '__main__':
    for sample in load():
        print(sample)

