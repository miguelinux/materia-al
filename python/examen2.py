#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab spelllang=es spell:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Examen II
"""

import alumnos
from ecuaciones_lineales import problema_de_ecuaciones_lineales


def main():
    """
    Comentario de la función
    """
    lista = alumnos.leer_alumnos("alumnos.csv")
    problema_de_ecuaciones_lineales()


if __name__ == "__main__":
    main()