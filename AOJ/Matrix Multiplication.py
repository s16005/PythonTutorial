n, m, l = [int(i) for i in input().split()]

A = []
B = []
C = []

for ni in range(n):
    A.append([int(i) for i in input().split()])

for mi in range(m):
    B.append([int(i) for i in input().split()])

for i in range(n):
    C.append([])
    for j in range(l):
        C[i].append(0)
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]

for ni in range(n):
    print(" ".join([str(s) for s in C[ni]]))
