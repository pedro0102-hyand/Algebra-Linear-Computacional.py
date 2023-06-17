def lu(A):
    n = len(A)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]
    P = [[0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
    for i in range(n):
        P[i][i] = 1
    for k in range(n):
        max_valor = abs(A[k][k])
        max_linha = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > max_valor:
                max_valor = abs(A[i][k])
                max_linha = i
        A[k], A[max_linha] = A[max_linha], A[k]
        P[k], P[max_linha] = P[max_linha], P[k]
        for i in range(k, n):
            U[k][i] = A[k][i]
        for i in range(k + 1, n):
            L[i][k] = A[i][k] // U[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - L[i][k] * U[k][j]
    return P, L, U
A = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     [1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
     [3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
     [4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
     [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
     [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
     [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3],
     [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2],
     [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
P, L, U = lu(A)
print("P:")
for linha in P:
    print(" ".join(str(num) for num in linha))
print("L:")
for linha in L:
    print(" ".join(str(num) for num in linha))
print("U:")
for linha in U:
    print(" ".join(str(num) for num in linha))
