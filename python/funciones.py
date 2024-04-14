# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab spelllang=es spell:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Modulo de funciones comunes del proyecto
"""

from random import randint


def aleatorio(inicio, fin):
    """Genera un número aleatorio entre inicio y fin.
    También le agrega un signo aleatoriamente"""
    # [B311:blacklist] Standard pseudo-random generators are not suitable
    # for security/cryptographic purposes.
    ret = randint(inicio, fin)  # nosec B311
    if ret and randint(0, 1):  # nosec B311
        ret = -ret
    return ret
