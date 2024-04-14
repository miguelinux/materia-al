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


def genera_matriz(filas, columnas):
    pass


def imprime_matrices(*matrices):
    pass


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
    m1 = aleatorio(1, 3)
    n1 = aleatorio(1, 3)

    if operacion == 1 or operacion == 2:
        # Si es suma o resta la matriz 1 y 2 son de la misma dimensión
        m2 = m1
        n2 = n1
    elif operacion == 3:
        # Si es multiplicación m2 = n1
        m2 = n1
        n2 = aleatorio(1, 3)
    elif operacion == 4:
        # Si es determinante son matrices cuadradas de 2x2 o 3x3
        m1 = aleatorio(2, 3)
        n1 = m1

    matriz_1 = genera_matriz(m1, n1)
    if operacion != 4:
        matriz_2 = genera_matriz(m2, n2)

    print("Resuelve la siguiente operación de matrices:\n")

    if operacion == 1:
        print("\n  Suma las siguientes matrices\n")
        imprime_matrices(matriz_1, matriz_2)
    elif operacion == 2:
        print("\n  Resta las siguientes matrices\n")
        imprime_matrices(matriz_1, matriz_2)
    elif operacion == 3:
        print("\n  Multiplica las siguientes matrices\n")
        imprime_matrices(matriz_1, matriz_2)
    elif operacion == 4:
        print("\n  Calcula el determinante de la siguiente matriz\n")
        imprime_matrices(matriz_1)
