def lu(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    P = [[0] * 1 for _ in range(n)]
    for i in range(n):
        L[i][i] = 1.0
    for i in range(n):
        P[i][0] = i
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
            L[i][k] = A[i][k] / U[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - L[i][k] * U[k][j]
    return P, L, U
def resolver_fatorizacao_LU(A, b):
    P, L, U = lu(A)
    n = len(A)
    y = [0.0] * n
    x = [0.0] * n
    b_permutado = [b[i] for i in range(n)]
    for k in range(n):
        b_permutado[k], b_permutado[P[k][0]] = b_permutado[P[k][0]], b_permutado[k]
    for i in range(n):
        y[i] = b_permutado[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x
A = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
    [3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
    [4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
    [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
    [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
    [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3],
    [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]
b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]
x = resolver_fatorizacao_LU(A, b)
print("Solução:")
print(x)

