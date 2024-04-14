# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab spelllang=es spell:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Modulo de alumnos
"""


def leer_alumnos(nombre_del_archivo_csv):
    """
    Lee los alumnos del archivo
    """
    lista_alumnos = []

    with open(nombre_del_archivo_csv, "r", encoding="utf8") as archivo:
        # Leemos la linea de encabezado
        linea = archivo.readline()

        for linea in archivo:
            lista = linea.strip().split(",")
            si_vino = False
            if lista[4]:
                si_vino = True
            alumno = {
                "matricula": lista[1],
                "nombre": lista[3],
                "apellidos": lista[2],
                "vino": si_vino,
            }
            lista_alumnos.append(alumno)

    return lista_alumnos
