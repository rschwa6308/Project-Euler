# Dijkstra's Algorithm should work fine


INFTY = 10000000000000

MAT = []

with open("p083_matrix.txt") as f:
    for line in f.readlines():
        row = []
        for n in line.split(","):
            row.append(int(n))
        MAT.append(row)


min_mat = [[INFTY for _ in range(80)] for _ in range(80)]

min_mat[0][0] = MAT[0][0]

def neighbors(x, y):
    neighbors = set()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 80 and 0 <= ny < 80:
            neighbors.add((nx, ny))
    
    return neighbors


unvisited = set((x, y) for x in range(80) for y in range(80))

while unvisited:
    cx, cy = min(unvisited, key=lambda item: min_mat[item[1]][item[0]])

    # mark current node as visited
    unvisited.remove((cx, cy))

    unvisited_neighbors = neighbors(cx, cy) & unvisited

    for (nx, ny) in unvisited_neighbors:
        min_mat[ny][nx] = min(
            min_mat[ny][nx],
            min_mat[cy][cx] + MAT[ny][nx]
        )


# for row in MAT[:5]:
#     print(" ".join(str(n).ljust(6) for n in row[:5]))

# print("-"*50)

# for row in min_mat[:5]:
#     print(" ".join(str(n).ljust(6) for n in row[:5]))


print(min_mat[-1][-1])

# => 425185
