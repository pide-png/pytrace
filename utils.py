import numpy as np


def lerp(a, b, t):
    return (1 - t) * a + t * b


def normalize(v):
    return v / np.linalg.norm(v)


# noinspection PyShadowingNames
def ray_trace(origin, direction, hitables, ambient, lights, max_reflections):
    max_reflections -= 1
    if max_reflections != 0:
        intersected_hitables = []
        for hitable in hitables:
            if hitable.intersect(direction, origin):
                intersected_hitables.append(hitable)
        try:
            closest_object = sorted(intersected_hitables, key=(lambda hitable: hitable.intersect(direction, origin)))[0]
            return closest_object.get_color(origin, direction, ambient, lights, hitables, max_reflections)
        except IndexError:
            return np.array([0, 0, 0])
