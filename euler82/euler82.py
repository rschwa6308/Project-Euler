from pprint import pprint


INFTY = 10000000000000

MAT = []

with open("p082_matrix.txt") as f:
    for line in f.readlines():
        row = []
        for n in line.split(","):
            row.append(int(n))
        MAT.append(row)




min_mat = [[None for _ in range(80)] for _ in range(80)]

# initialize left column
for y in range(80):
    min_mat[y][0] = MAT[y][0]

for x in range(1, 80):
    for y in range(80):
        # determine the value of min_mat[y][x]
        # it comes from either RD+ or RU+
        options = []
        for start_y in range(80):
            if start_y <= y:
                options.append(min_mat[start_y][x-1] + sum(MAT[i][x] for i in range(start_y, y)))
            else:
                options.append(min_mat[start_y][x-1] + sum(MAT[i][x] for i in range(start_y, y, -1)))


        val = min(options) + MAT[y][x]
        min_mat[y][x] = val



# for row in MAT:
#     print(" ".join(str(n).ljust(6) for n in row[-5:]))

# print("-"*50)

# for row in min_mat:
#     print(" ".join(str(n).ljust(6) for n in row[-5:]))





print(min(row[-1] for row in min_mat))


# => 260324




# def least_path_sum(target_x, target_y):

    # min_mat = [[None for _ in range(80)] for _ in range(80)]

    # # initialize left column
    # for y in range(80):
    #     min_mat[y][0] = MAT[y][0]

#     def min_path(x, y, columns_up_used, columns_down_used):
#         print(f"{x=} {y=}")
#         print(f"{columns_up_used=} {columns_down_used=}")
#         if x < 0 or y < 0 or x > 79 or y > 79:
#             return INFTY
        
#         if min_mat[y][x] is not None:
#             return min_mat[y][x]
        
#         val = INFTY

#         options = []

#         # left
#         options.append(min_path(x - 1, y, columns_up_used, columns_down_used))

#         # up
#         if x not in columns_down_used:
#             options.append(min_path(x, y - 1, columns_up_used | {x}, columns_down_used))

#         # down
#         if x not in columns_up_used:
#             options.append(min_path(x, y + 1, columns_up_used, columns_down_used | {x}))

#         val = min(options) + MAT[y][x]
#         min_mat[y][x] = val

#         return val


#     return min_path(target_x, target_y, set(), set())


# print(min(least_path_sum(79, y) for y in range(80)))
