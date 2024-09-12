# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab spelllang=es spell:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Modulo de complejos
"""

from cmath import polar
from math import degrees
from random import randint

from funciones import aleatorio

def problema_de_complejos():
    """Muestra el problema de números complejos"""

    r1 = aleatorio(0, 4)
    i1 = aleatorio(1, 4)
    r2 = aleatorio(1, 4)
    i2 = aleatorio(0, 4)

    z1 = complex(r1,i1)
    z2 = complex(r2,i2)

    operacion = randint(1,6)

    print("z1 =", z1)
    print("z2 =", z2)
    print("\n¿Cuál es el resultado de ", end="")

    if operacion == 1: # Suma
        print("la suma de z1 y z2?")
        z3 = z1 + z2
    elif operacion == 2: # Resta
        print("la resta de z1 y z2?")
        z3 = z1 - z2
    elif operacion == 3: # Multiplicación
        print("la multiplicación de z1 y z2?")
        z3 = z1 * z2
    elif operacion == 4: # División
        print("la división de z1 y z2?")
        z3 = z1 / z2
    elif operacion == 5: # Conjugado
        print("el conjugado de z1?")
        z3 = z1.conjugate()
    elif operacion == 6: # Forma polar (r,thetha)
        print("la forma polar de z1?")
        r, theta = polar(z1)
        theta = degrees(theta)

    # Esperamos a que den un enter
    input("\nIngresa un Enter para mostrar la respuesta:")

    print("\nEl resutlado es:  ", end="")

    if operacion == 6:
        print("r=",r,"  theta=", theta)
    else:
        print("z3=",z3)

    print("\n-------------------\n")

