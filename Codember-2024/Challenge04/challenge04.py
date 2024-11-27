'''
Desafío 5: ¡Encuentra a ΩMEGA!

Necesitamos encontrar los números que cumplen las siguientes condiciones:

El número es primo.

La suma de sus dígitos también es un número primo.

Tu tarea es escribir un programa que encuentre cuántos números de la lista 
cumplen con estas condiciones y determinar cuál es el tercer número que cumple 
con ellas al recorrer la lista en orden ascendente.
'''
import sys
sys.path.append('Codember-2024/Challenge03/')
from challenge03 import safeNodes

def isPrime(num: int):
    for i in range(2, num):
        if (num % i == 0):
            return False;
    return True

def sumDigitsPrime(num: int):
    res = 0  
    while(num > 0):
        digit = num % 10
        num //= 10
        res += digit
    if (isPrime(res)): return True
    else: return False

def findOmega(safeNodes: list):
    res = []
    for node in safeNodes:
        if isPrime(node) and sumDigitsPrime(node):
            res.append(node)
    return res

if __name__ == "__main__":
    with open("Codember-2024/Challenge03/network.txt") as file:
        for line in file:
            nodes = eval(line);
            getSafeNodes = safeNodes(nodes)
            Omega = findOmega(getSafeNodes)
            print(f'\nsubmit {len(Omega)}-{Omega[2]}')