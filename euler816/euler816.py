from itertools import combinations
from math import sqrt

import numpy as np
from scipy.spatial import KDTree

def generate_points(k):
    sequence = [290797]
    for _ in range(k-1):
        sequence.append((sequence[-1]**2) % 50515093)
    
    points = [(sequence[2*i], sequence[2*i+1]) for i in range(k//2)]
    return np.array(points)


def shortest_distance(points):
    tree = KDTree(points)

    # get nearest neighbors
    res, _ = tree.query(points, k=2)

    # exclude distance to self (always 0.0)
    distances = res[:,1]

    return np.min(distances)


def d(k):
    points = generate_points(2*k)
    return shortest_distance(points)


assert(round(d(14), 9) == 546446.466846479) 

if __name__ == "__main__":
    answer = d(2_000_000)
    print(round(answer, 9))
