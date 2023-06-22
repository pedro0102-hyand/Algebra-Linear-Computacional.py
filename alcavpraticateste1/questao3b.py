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
def criar_identidade(n):
    identidade = [[0.0] * n for _ in range(n)]
    for i in range(n):
        identidade[i][i] = 1.0
    return identidade
def multiplicar_matrizes(A, B):
    linhas_A = len(A)
    colunas_A = len(A[0])
    linhas_B = len(B)
    colunas_B = len(B[0])
    if colunas_A != linhas_B:
        raise ValueError("As matrizes não podem ser multiplicadas. O número de colunas de A deve ser igual ao número de linhas de B.")
    resultado = [[0.0] * colunas_B for _ in range(linhas_A)]
    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado
def calcular_inversa(A):
    n = len(A)
    identidade = criar_identidade(n)
    P, L, U = lu(A)
    inversa = []
    for i in range(n):
        coluna_i = [identidade[j][i] for j in range(n)]
        x = resolver_fatorizacao_LU(A, coluna_i)
        inversa.append(x)
    inversa = [[linha[i] for linha in inversa] for i in range(n)]  
    return inversa
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
inversa = calcular_inversa(A)
print("Inversa:")
for linha in inversa:
    linha_formatada = ["{:.2f}".format(elemento) for elemento in linha]
    print(" ".join(linha_formatada))

