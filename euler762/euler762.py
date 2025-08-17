grid_lists = [
    set(["0,0"])
]




def parse_grid_string(grid_string):
    amoebas = set()
    for item in grid_string.split(";"):
        x, _, y = item.partition(",")
        amoebas.add((int(x), int(y)))
    return amoebas

def amoebas_to_grid_string(amoebas):
    return ";".join([f"{x},{y}" for (x, y) in sorted(amoebas, key=lambda a: 1000*a[0]+a[1])])


def compute_splits(grid_string):
    amoebas = parse_grid_string(grid_string)

    splits = set()
    for (x, y) in amoebas:
        if (x+1, y) not in amoebas and (x+1, (y+1)%4) not in amoebas:
            # a split is possible
            new_amoebas = set(amoebas)
            new_amoebas.remove((x, y))
            new_amoebas.add((x+1, y))
            new_amoebas.add((x+1, (y+1)%4))
            splits.add(amoebas_to_grid_string(new_amoebas))

    return splits


# print(compute_splits("0,0"))
# print(compute_splits('1,0;0,1'))

N = 16

# for n in range(1, N+1):
#     grid_lists.append(set())

#     for grid in grid_lists[n-1]:
#         grid_lists[n] |= compute_splits(grid)

#     # print(n, len(grid_lists[n]))
#     print(len(grid_lists[n]))
    


# Related sequence: https://oeis.org/A007902
# (seems to match up to N=16 ???)


    

import numpy as np

G_table = np.full((N+2, N+2), -1, dtype=int)

G_table[0] = 0

def G(k, m):
    print(f"G({k}, {m})")
    # m = m % 4

    if k < 0 or m < 0: return 0

    if G_table[k, m] != -1:
        return G_table[k, m]

    if m == 0:
        val = 2 * G(k-1, 0) + G(k, 1) + (1 if k == 2 else 0)
    
    elif m == 1:
        val = G(k-3, 0) + 2 * G(k-2, 1) + G(k-1, 2) + G(k-4, 1)
    
    else:
        val = G(k-m-2, m-1) + 2 * G(k-m-1, m) + G(k-m, m+1)

    G_table[k, m] = val
    return val


print(G(N+1, 0))