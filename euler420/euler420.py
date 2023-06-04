from itertools import combinations
from math import sqrt


def matrix_square_root(A, B, C, D):
    trace = A+D
    det = A*D - B*C
    
    s = sqrt(det)

    if s.is_integer():
        s = int(s)
    else:
        raise ValueError("No integer sqrt exists")

    t1 = sqrt(trace + 2*s)
    t2 = sqrt(trace - 2*s)

    if t1.is_integer():
        t1 = int(t1)
    else:
        raise ValueError("No integer sqrt exists")
    if t2.is_integer():
        t2 = int(t2)
    else:
        raise ValueError("No integer sqrt exists")

    return ((A+s)/t1, B/t1, C/t1, (D+s)/t1), ((A-s)/t2, B/t2, C/t2, (D-s)/t2)


# print(matrix_square_root(40, 12, 48, 40))
# print(matrix_square_root(17, 1, 47, 63))
# print(matrix_square_root(33, 1, 527, 47))



def factorizations(N):
    total = 0
    for d in range(1, int(sqrt(N))+1):
        if N % d == 0:
            yield (d, N//d)
            if d != N//d:
                yield (N//d, d)



def count_matrices(trace, det):
    "Count the number of possible positive integer matrices with specified trace and determinant"

    sqrt_det = int(sqrt(det))

    total = 0
    for A in range(1, trace):
        D = trace - A
        if A <= sqrt_det or D <= sqrt_det: continue

        res = A*D - det
        if res <= 0: continue

        for B, C in factorizations(res):
            sqrt1, sqrt2 = matrix_square_root(A, B, C, D)
            if all(n > 0 and n.is_integer() for n in sqrt1) and all(n > 0 and n.is_integer() for n in sqrt2):
                total += 1
                print(A, B, C, D)

    return total



# print(count_matrices(40+40, 40*40-12*48))
#                      80       1024



def F(N):
    squares = [n**2 for n in range(1, int(sqrt(N)) + 1) if n**2 < N]

    possible_trace_dets = []
    for s1, s2 in combinations(squares, 2):
        if (s1 - s2)%2 == 1: continue
        t = (s1 + s2)//2
        d = ((s2-t)//2)**2
        possible_trace_dets.append((t, d))

    # print(len(possible_trace_dets))
    # print(possible_trace_dets[:10])

    total = 0
    for trace, det in possible_trace_dets:
        ms = count_matrices(trace, det)
        print(f"trace={trace}, det={det} ===> {ms}")
        total += count_matrices(trace, det)
    
    return total



assert F(50) == 7
# assert F(1000) == 1019

# print(F(10**7))

# # => 
