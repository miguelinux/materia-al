#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab spelllang=es spell:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Examen I
"""

from random import randint

from alumnos import leer_alumnos
from complejos import problema_de_complejos


def main():
    """
    Comentario de la función
    """
    lista = leer_alumnos("alumnos.csv")
    tam = len(lista)

    for _ in range(tam):
        # [B311:blacklist] Standard pseudo-random generators are not suitable
        # for security/cryptographic purposes.
        siguiente = randint(0, len(lista) - 1)  # nosec B311
        alumno = lista[siguiente]
        lista.pop(siguiente)
        print("Por favor\n\n", alumno["nombre"], alumno["apellidos"], end="")
        if alumno["vino"]:
            print("  (Si vino)")
        else:
            print()
        print("\npasa al pizarrón y \n")

        problema_de_complejos()
        problema_de_complejos()

        # Esperamos a que den un enter
        input("Da un enter para continuar:")


if __name__ == "__main__":
    main()
