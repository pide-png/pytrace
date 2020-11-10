import numpy as np


def lerp(a, b, t):
    return (1 - t) * a + t * b


def normalize(v):
    return v / np.linalg.norm(v)
