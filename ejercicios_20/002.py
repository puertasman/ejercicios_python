# primeros ejercicios
from math import pi
from typing import TypeVar
#from hypothesis import given
#from hypothesis import strategies as st
A = TypeVar('A')

# ---------------------------------------------------------------------
# Ejercicio 11. Definir la función
# interior : (list[A]) -> list[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
# interior([2, 5, 3, 7, 3]) == [5, 3, 7]
# ---------------------------------------------------------------------
print(20*"-")
def interior(lista: list[A]) -> list[A]:
    return (lista[1:-1])

print(interior([2, 5, 3, 7, 3]))

# ---------------------------------------------------------------------
# Ejercicio 12
# Definir la función
# finales : (int, list[A]) -> list[A]
# tal que finales(n, xs) es la lista formada por los n finales
# elementos de xs. Por ejemplo,
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]
# ---------------------------------------------------------------------
print(20*"-")
def finales(n: int, xs: list[A]) -> list[A]:
    return xs[-n:]

print(finales(3, [2, 5, 4, 7, 9, 6]))