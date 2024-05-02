# primeros ejercicios
from math import pi
from typing import TypeVar
#from hypothesis import given
#from hypothesis import strategies as st
A = TypeVar('A')

# ---------------------------------------------------------------------
# Ejercicio 1. Definir la función
# media3 : (float, float, float) -> float
# tal que (media3 x y z) es la media aritmética de los números x, y y
# z. Por ejemplo,
# media3(1, 3, 8) == 4.0
# media3(-1, 0, 7) == 2.0
# media3(-3, 0, 3) == 0.0
# ---------------------------------------------------------------------
print(20*"-")
def media3(x: float, y: float,z: float) -> float:
    return (x + y + z ) / 3
print(media3(1, 3, 8))
print(media3(-1, 0, 7))
print(media3(-3, 0, 3))

# ---------------------------------------------------------------------
# Ejercicio 2. Definir la función
# sumaMonedas : (int, int, int, int, int) -> int
# tal que sumaMonedas(a, b, c, d, e) es la suma de los euros
# correspondientes a a monedas de 1 euro, b de 2 euros, c de 5 euros, d
# 10 euros y e de 20 euros. Por ejemplo,
# sumaMonedas(0, 0, 0, 0, 1) == 20
# sumaMonedas(0, 0, 8, 0, 3) == 100
# sumaMonedas(1, 1, 1, 1, 1) == 38
# ---------------------------------------------------------------------
print(20*"-")
def sumaMonedas(a: int, b: int, c: int, d: int, e: int ) -> int:
    return (a * 1 + b * 2 + c * 5 + d * 10 + e * 20)
print(sumaMonedas(0, 0, 0, 0, 1))
print(sumaMonedas(0, 0, 8, 0, 3))
print(sumaMonedas(1, 1, 1, 1, 1))

# ---------------------------------------------------------------------
# Ejercicio 3. Definir la función
# volumenEsfera : (float) -> float
# tal que volumenEsfera(r) es el volumen de la esfera de radio r. Por
# ejemplo,
# volumenEsfera(10) == 4188.790204786391
# ---------------------------------------------------------------------
print(20*"-")
def volumenEsfera (radio: float) -> float:
    return (4 / 3) * pi * radio ** 3

print(volumenEsfera(10))

# ---------------------------------------------------------------------
# Ejercicio 4. Definir la función
# areaDeCoronaCircular : (float, float) -> float
# tal que areaDeCoronaCircular(r1, r2) es el área de una corona
# circular de radio interior r1 y radio exterior r2. Por ejemplo,
# areaDeCoronaCircular(1, 2) == 9.42477796076938
# areaDeCoronaCircular(2, 5) == 65.97344572538566
# areaDeCoronaCircular(3, 5) == 50.26548245743669
# ---------------------------------------------------------------------
print(20*"-")
def areaDeCoronaCircular(r1 : float, r2: float) -> float:
    return pi * (r2 ** 2 - r1 ** 2)

print(areaDeCoronaCircular(1, 2))
print(areaDeCoronaCircular(2, 5))
print(areaDeCoronaCircular(3, 5))

# ---------------------------------------------------------------------
# Ejercicio 5. Definir la función
# ultimoDigito : (int) -> int
# tal que ultimoDigito(x) es el último dígito del número x. Por
# ejemplo,
# ultimoDigito(325) == 5
# ---------------------------------------------------------------------
print(20*"-")
def ultimoDigito(num: int) -> int:
    return num % 10
    # versión más rebuscada return int(str(num)[-1])

print(ultimoDigito(325))
print(ultimoDigito(0))

# ---------------------------------------------------------------------
# Ejercicio 6. Definir la función
# maxTres : (int, int, int) -> int
# tal que maxTres(x, y, z) es el máximo de x, y y z. Por ejemplo,
# maxTres(6, 2, 4) == 6
# maxTres(6, 7, 4) == 7
# maxTres(6, 7, 9) == 9
# ---------------------------------------------------------------------
print(20*"-")
def maxTres(x: int, y: int, z: int) -> int:
    if (x > y):
        if (x > z):
            return x
        else:
            return z
    else:
        if (y > z):
            return y
        else:
            return z
        
    # version facil return max(x, y, z)
        
print(maxTres(6, 2, 4))
print(maxTres(6, 7, 4))
print(maxTres(6, 7, 9))

# ---------------------------------------------------------------------
# Ejercicio 7. Definir la función
# rota1 : (List[A]) -> List[A]
# tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
# xs al final de la lista. Por ejemplo,
# rota1([3, 2, 5, 7]) == [2, 5, 7, 3]
# rota1(['a', 'b', 'c']) == ['b', 'c', 'a']
# ---------------------------------------------------------------------
print(20*"-")
def rota1(a: list[A]) -> list[A]:
    if a == []:
        return a
    else:
        return a[1:]
    return a

print(rota1([3, 2, 5, 7]))
print(rota1(['a', 'b', 'c']))

# ---------------------------------------------------------------------
# Ejercicio 8. Definir la función
# rota : (int, List[A]) -> List[A]
# tal que rota(n, xs) es la lista obtenida poniendo los n primeros
# elementos de xs al final de la lista. Por ejemplo,
# rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3]
# rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2]
# rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]
# ---------------------------------------------------------------------
print(20*"-")
def rota(n: int, lista: list[A]) -> list[A]:
    return lista[n:] + lista [:n]

print(rota(1, [3, 2, 5, 7]))
print(rota(2, [3, 2, 5, 7]))
print(rota(3, [3, 2, 5, 7]))

# ---------------------------------------------------------------------
# Ejercicio 9. Definir la función
# rango : (List[int]) -> List[int]
# tal que rango(xs) es la lista formada por el menor y mayor elemento
# de xs.
# rango([3, 2, 7, 5]) == [2, 7]
# ---------------------------------------------------------------------
print(20*"-")
def rango(lista: list[int]) -> list[int]:
    return [min(lista), max(lista)]

print(rango([3, 2, 7, 5]))

# ---------------------------------------------------------------------
# Ejercicio 10. Definir la función
# palindromo : (List[A]) -> bool
# tal que palindromo(xs) se verifica si xs es un palíndromo; es decir,
# es lo mismo leer xs de izquierda a derecha que de derecha a
# izquierda. Por ejemplo,
# palindromo([3, 2, 5, 2, 3]) == True
# palindromo([3, 2, 5, 6, 2, 3]) == False
# ---------------------------------------------------------------------
print(20*"-")
def palindromo (lista: list[A]) -> bool:
    return lista == lista[::-1]
print(palindromo([3, 2, 5, 2, 3]))
print(palindromo([3, 2, 5, 6, 2, 3]))