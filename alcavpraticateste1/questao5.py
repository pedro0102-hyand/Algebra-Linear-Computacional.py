def gauss_jacobi(A, b, x0, max_iteracoes, tolerancia):
    n = len(A)
    x = x0.copy()
    iteracoes = 0
    norm_diff = tolerancia + 1
    while iteracoes < max_iteracoes and norm_diff > tolerancia:
        x_new = x.copy()
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]
        norm_diff = max(abs(x_new[i] - x[i]) for i in range(n))
        x = x_new
        iteracoes += 1
    return x, iteracoes
def gauss_seidel(A, b, x0, max_iteracoes, tolerancia):
    n = len(A)
    x = x0.copy()
    iteracoes = 0
    norm_diff = tolerancia + 1
    while iteracoes < max_iteracoes and norm_diff > tolerancia:
        x_new = x.copy()
        for i in range(n):
            sum_ax = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]
        norm_diff = max(abs(x_new[i] - x[i]) for i in range(n))
        x = x_new
        iteracoes += 1
    return x, iteracoes
def sor(A, b, x0, max_iteracoes, tolerancia, omega):
    n = len(A)
    x = x0.copy()
    iteracoes = 0
    norm_diff = tolerancia + 1
    while iteracoes < max_iteracoes and norm_diff > tolerancia:
        x_new = x.copy()
        for i in range(n):
            sum_ax = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sum_ax)
        norm_diff = max(abs(x_new[i] - x[i]) for i in range(n))
        x = x_new
        iteracoes += 1
    return x, iteracoes
n = 20
h = 0.1
A = [[0] * (n + 1) for _ in range(n + 1)]
b = [0] * (n + 1)
A[0][0] = -2 * (1 + h ** 2)
A[0][1] = 1
b[0] = 1
for i in range(1, n):
    A[i][i - 1] = 1
    A[i][i] = -2 * (1 + h ** 2)
    A[i][i + 1] = 1
A[n][n - 1] = 1
A[n][n] = -2 * (1 + h ** 2)
b[n] = 1
x0 = [0] * (n + 1)
max_iteracoes = 1000
tolerancia = 1e-4
omega = 1.5
x_jacobi, iteracoes_jacobi = gauss_jacobi(A, b, x0, max_iteracoes, tolerancia)
x_seidel, iteracoes_seidel = gauss_seidel(A, b, x0, max_iteracoes, tolerancia)
x_sor, iteracoes_sor = sor(A, b, x0, max_iteracoes, tolerancia, omega)
# Imprimindo os resultados
print("Método de Gauss-Jacobi:")
print("Número de iterações:", iteracoes_jacobi)
print("Solução aproximada:")
for i, value in enumerate(x_jacobi):
    print(f"x[{i}] =", value)
print()
print("Método de Gauss-Seidel:")
print("Número de iterações:", iteracoes_seidel)
print("Solução aproximada:")
for i, value in enumerate(x_seidel):
    print(f"x[{i}] =", value)
print()
print("Método SOR:")
print("Número de iterações:", iteracoes_sor)
print("Solução aproximada:")
for i, value in enumerate(x_sor):
    print(f"x[{i}] =", value)
print()
