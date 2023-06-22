
def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                temp_soma = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = (A[i][j] - temp_soma) ** 0.5
            else:
                temp_soma = sum(L[i][k] * L[j][k] for k in range(j))
                if L[j][j] != 0:
                    L[i][j] = (A[i][j] - temp_soma) / L[j][j]
                else:
                    raise ValueError("A não é simétrica definida positiva")
    return L
def simetrica(A):
    n = len(A)
    for i in range(n):
        for j in range(i):
            if A[i][j] != A[j][i]:
                return False
    return True
def definitiva(A):
    if not simetrica(A):
        return False
    try:
        cholesky(A)
    except ValueError:
        return False
    return True
# Exemplo de uso
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
if definitiva(A):
    L = cholesky(A)
    print("A é simétrica definida positiva.")
    print("Fatoração de Cholesky L:")
    for linha in L:
        print(linha)
else:
    print("A não é simétrica definida positiva.")
