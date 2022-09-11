"""
32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de
seu dobro.
"""
numero = int(input('Digite um numero: '))
antecessor = numero * 2 - 1
sucessor = numero * 3 + 1
soma = antecessor + sucessor

print(f'O resultado é {soma}')
