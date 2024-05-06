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

# ---------------------------------------------------------------------
# Ejercicio 13. Definir la función
# segmento : (int, int, list[A]) -> list[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
# segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
# segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
# segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
# ---------------------------------------------------------------------
print (20*"-")
def segmento(m: int, n: int, xs: list[A] -> list[A]:
    return xs[m+1:n]
segmento(3, 4, [3, 4, 1, 2, 7, 9, 0])
segmento(3, 5, [3, 4, 1, 2, 7, 9, 0])
segmento(5, 3, [3, 4, 1, 2, 7, 9, 0])

# ---------------------------------------------------------------------
# Ejercicio 14. Definir la función
# extremos : (int, list[A]) -> list[A]
# tal que extremos(n, xs) es la lista formada por los n primeros
# elementos de xs y los n finales elementos de xs. Por ejemplo,
# extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]
# ---------------------------------------------------------------------
print(20*"-")
def extremos(n: int, xs: list[A]) -> list[A]:
    return xs[:n] + xs[-n:]
extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3])

# ---------------------------------------------------------------------
# Ejercicio 15. Definir la función
# mediano : (int, int, int) -> int
# tal que mediano(x, y, z) es el número mediano de los tres números x, y
# y z. Por ejemplo,
# mediano(3, 2, 5) == 3
# mediano(2, 4, 5) == 4
# mediano(2, 6, 5) == 5
# mediano(2, 6, 6) == 6
# ---------------------------------------------------------------------
print(20*"-")
def mediano(x: int, y: int, z:int) -> int:
    return x + y + z - min([x,y,z]) - max([x,y,z])

mediano(3, 2, 5)
mediano(2, 4, 5)
mediano(2, 6, 5)
mediano(2, 6, 6)

# ---------------------------------------------------------------------
# Ejercicio 16. Definir la función
# tresIguales : (int, int, int) -> bool
# tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
# iguales. Por ejemplo,
# tresIguales(4, 4, 4) == True
# tresIguales(4, 3, 4) == False
# ---------------------------------------------------------------------
print(20*'-')
def tresIguales(x:int, y: int, z:int) -> bool:
    return x == y == z
tresIguales(4, 4, 4)
tresIguales(4, 3, 4)

# ---------------------------------------------------------------------
# Ejercicio 17. Definir la función
# tresDiferentes : (int, int, int) -> bool
# tal que tresDiferentes(x, y, z) se verifica si los elementos x, y y z
# son distintos. Por ejemplo,
# tresDiferentes(3, 5, 2) == True
# tresDiferentes(3, 5, 3) == False
# ---------------------------------------------------------------------
print(20*'-')
def tresDiferentes(x:int, y: int, z:int) -> bool:
    return x != y  and x != z and y != z

tresDiferentes(3, 5, 2)
tresDiferentes(3, 5, 3)

# ---------------------------------------------------------------------
# Ejercicio 18. Definir la función
# cuatroIguales : (int, int, int, int) -> bool
# tal que cuatroIguales(x,y,z,u) se verifica si los elementos x, y, z y
# u son iguales. Por ejemplo,
# cuatroIguales(5, 5, 5, 5) == True
# cuatroIguales(5, 5, 4, 5) == False
# ---------------------------------------------------------------------
print(20*'-')
def cuatroIguales(x: int, y: int, z: int, u:int)->bool:
    return x == y and tresIguales(y,z,u)
cuatroIguales(5, 5, 5, 5)
cuatroIguales(5, 5, 4, 5)
