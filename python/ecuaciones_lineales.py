# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab spelllang=es spell:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Modulo de ecuaciones lineales
"""

from random import randint

from funciones import aleatorio


def str_ecuacion(a, b, c):
    """Regresa una ecuación de la forma Ax + By = C"""
    ret = "    "
    if a:
        ret = f"{a:2}x "
    if b:
        ret += f"{b:=+3}y = {c:2}"
    else:
        ret += f"     = {c:2}"
    return ret


def problema_de_ecuaciones_lineales():
    """Muestra el problema de ecuaciones lineales"""
    #  A1x + B1y = C1
    #  A2x + B2y = C2
    a1 = aleatorio(0, 5)
    b1 = aleatorio(0, 5)
    c1 = aleatorio(0, 5)
    a2 = aleatorio(0, 5)
    b2 = aleatorio(0, 5)
    c2 = aleatorio(0, 5)

    metodos = (
        "sustitución",
        "igualación",
        "eliminación/reducción (suma,resta)",
        "Cramer (determinantes)",
    )
    cual = randint(0, 3)  # nosec B311
    print("Resuelve el siguiente sistema de ecuaciones,")
    print("por el método de", metodos[cual], ":\n")

    print(str_ecuacion(a1, b1, c1))
    print(str_ecuacion(a2, b2, c2), "\n")

    # Determinante del sistema X Y
    #  | A1   B1 |
    #  | A2   B2 |
    determinante = a1 * b2 - a2 * b1

    # Esperamos a que den un enter
    input("Ingresa un Enter para mostrar la respuesta:")

    if determinante:
        # Determinante sustituyendo X
        #  | C1   B1 |
        #  | C2   B2 |
        determinante_x = c1 * b2 - c2 * b1

        # Determinante sustituyendo Y
        #  | A1   C1 |
        #  | A2   C2 |
        determinante_y = a1 * c2 - a2 * c1

        # Sacamos la solución
        x = determinante_x / determinante
        y = determinante_y / determinante

        print("La solución es:")
        print(f"  X = {determinante_x}/{determinante} = {x}")
        print(f"  Y = {determinante_y}/{determinante} = {y}")
    else:
        print("El Determinante del sistema es cero, por lo tanto")
        print("el sistema no tiene solución ó tiene infinitas soluciones")
        print("ya que las ecuaciones o son paralelas o es la misma linea")
