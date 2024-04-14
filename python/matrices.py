# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab spelllang=es spell:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Modulo de operaciones con matrices
"""

from random import randint

from funciones import aleatorio


def suma(m1, m2):
    """Calcula la suma de dos matrices"""
    m = []
    for f, la_fila in enumerate(m1):
        m.append([])
        for c, valor in enumerate(la_fila):
            #  m1[f][c] + m2[f][c]
            m[f].append(valor + m2[f][c])
    return m


def resta(m1, m2):
    """Calcula la resta de dos matrices"""
    m = []
    for f, la_fila in enumerate(m1):
        m.append([])
        for c, valor in enumerate(la_fila):
            #  m1[f][c] - m2[f][c]
            m[f].append(valor - m2[f][c])
    return m


def multiplicacion(m1, m2):
    """Calcula la multiplicación de dos matrices"""
    m = []
    # Filas de la primera
    for f1, la_fila in enumerate(m1):
        m.append([])
        # Columnas de la segunda
        for c2 in range(len(m2[0])):
            la_suma = 0
            # Columnas de la primera y Filas de la segunda
            for c1f2, valor in enumerate(la_fila):
                # la_suma += m1[f1][c1f2] * m2[c1f2][c2]
                la_suma += valor * m2[c1f2][c2]
            m[f1].append(la_suma)
    return m


def determinante(m):
    """Calcula el determinante de una matriz"""
    if len(m) == 2:
        det = m[0][0] * m[1][1] - m[1][0] * m[0][1]
    else:
        det = m[0][0] * m[1][1] * m[2][2]
        det += m[0][1] * m[1][2] * m[2][0]
        det += m[0][2] * m[1][0] * m[2][1]
        det -= m[0][2] * m[1][1] * m[2][0]
        det -= m[0][0] * m[1][2] * m[2][1]
        det -= m[0][1] * m[1][0] * m[2][2]
    return det


def genera_matriz(filas, columnas):
    """Genera una matriz a partir de los argumentos filas y columnas"""
    m = []
    for f in range(filas):
        m.append([])
        for _ in range(columnas):
            m[f].append(aleatorio(0, 6))
    return m


def imprime_matrices(*matrices):
    """Imprime una o varias matrices ingresada en *matrices"""
    for m in matrices:
        for _, la_fila in enumerate(m):
            print("|", end="")
            for _, valor in enumerate(la_fila):
                # El valor es m[f][c]
                print(f"{valor:3}", end=" ")
            print("|")
        print()


def problema_de_matrices():
    """
    Muestra el problema de matrices

    1. Suma
    2. Resta
    3. Multiplicación
    4. Determinante
    """

    operacion = randint(1, 4)  # nosec B311

    # Matriz de mxn
    m1 = randint(1, 3)  # nosec B311
    n1 = randint(1, 3)  # nosec B311

    if operacion in (1, 2):
        # Si es suma o resta la matriz 1 y 2 son de la misma dimensión
        m1 = randint(2, 5)  # nosec B311
        n1 = randint(2, 5)  # nosec B311
        m2 = m1
        n2 = n1
    elif operacion == 3:
        # Si es multiplicación m2 = n1
        m2 = n1
        n2 = randint(1, 3)  # nosec B311
    elif operacion == 4:
        # Si es determinante son matrices cuadradas de 2x2 o 3x3
        m1 = randint(2, 3)  # nosec B311
        n1 = m1

    matriz_1 = genera_matriz(m1, n1)
    if operacion != 4:
        matriz_2 = genera_matriz(m2, n2)

    print("Resuelve la siguiente operación de matrices:\n")

    if operacion == 1:
        print("  Suma las siguientes matrices\n")
        imprime_matrices(matriz_1, matriz_2)
    elif operacion == 2:
        print("  Resta las siguientes matrices\n")
        imprime_matrices(matriz_1, matriz_2)
    elif operacion == 3:
        print("  Multiplica las siguientes matrices\n")
        imprime_matrices(matriz_1, matriz_2)
    elif operacion == 4:
        print("  Calcula el determinante de la siguiente matriz\n")
        imprime_matrices(matriz_1)

    # Esperamos a que den un enter
    input("Ingresa un Enter para mostrar la respuesta:")

    if operacion == 1:
        resultado = suma(matriz_1, matriz_2)
        print("El resultado es:")
        imprime_matrices(resultado)
    elif operacion == 2:
        resultado = resta(matriz_1, matriz_2)
        print("El resultado es:")
        imprime_matrices(resultado)
    elif operacion == 3:
        resultado = multiplicacion(matriz_1, matriz_2)
        print("El resultado es:")
        imprime_matrices(resultado)
    elif operacion == 4:
        resultado = determinante(matriz_1)
        print("El valor del determinante es:", resultado)
