def pivoteamento_total(A, b):
    n = len(A)
    permutacoes = list(range(n))
    for k in range(n-1):
        pivo_linha, pivot_column = k, k
        pivo = abs(A[k][k])
        for i in range(k, n):
            for j in range(k, n):
                if abs(A[i][j]) > pivo:
                    pivo = abs(A[i][j])
                    pivo_linha, pivo_column = i, j
        A[k], A[pivo_linha] = A[pivo_linha], A[k]
        b[k], b[pivo_linha] = b[pivo_linha], b[k]
        permutacoes[k], permutacoes[pivo_linha] = permutacoes[pivo_linha], permutacoes[k]
        for i in range(n):
            A[i][k], A[i][pivo_column] = A[i][pivo_column], A[i][k]
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k+1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
    x = [0] * n
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = b[i]
        for j in range(i+1, n):
            sum -= A[i][j] * x[j]
        x[i] = sum / A[i][i]
    x_permutado = [x[permutacoes[i]] for i in range(n)]
    return x_permutado
A = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    [3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    [4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
    [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
    [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
    [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
    [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
    [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3],
    [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2],
    [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]
b = [
    [0],
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10],
    [11],
    [12],
    [13],
    [14],
    [15],
    [16],
    [17],
    [18],
    [19],
    [20]
]
matriz_aumentada = []
for i in range(len(A)):
    matriz_aumentada.append(A[i] + b[i])
n = len(A)
for k in range(n-1):
    pivo_linha, pivo_column = k, k
    pivo = abs(matriz_aumentada[k][k])
    for i in range(k, n):
        for j in range(k, n+1):
            if abs(matriz_aumentada[i][j]) > pivo:
                pivo = abs(matriz_aumentada[i][j])
                pivo_linha, pivo_column = i, j
    matriz_aumentada[k], matriz_aumentada[pivo_linha] = matriz_aumentada[pivo_linha], matriz_aumentada[k]
    for i in range(n):
        matriz_aumentada[i][k], matriz_aumentada[i][pivo_column] = matriz_aumentada[i][pivo_column], matriz_aumentada[i][k]
    for i in range(k+1, n):
        factor = matriz_aumentada[i][k] / matriz_aumentada[k][k]
        matriz_aumentada[i][k] = 0
        for j in range(k+1, n+1):
            matriz_aumentada[i][j] -= factor * matriz_aumentada[k][j]
x = [0] * n
x[n-1] = matriz_aumentada[n-1][n] / matriz_aumentada[n-1][n-1]
for i in range(n-2, -1, -1):
    sum = matriz_aumentada[i][n]
    for j in range(i+1, n):
        sum -= matriz_aumentada[i][j] * x[j]
    x[i] = sum / matriz_aumentada[i][i]
for i in range(n):
    print(f"x[{i}] = {x[i]}")



