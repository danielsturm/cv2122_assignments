import numpy as np


def apply_erosion(prev, curr, next, index) -> bool:
    struct_elem_px = [
        curr[index - 1],
        curr[index + 1],
        prev[index],
        next[index],
    ]
    target = np.array([255, 255, 255])
    return all(np.array_equal(elem, target) for elem in struct_elem_px)
