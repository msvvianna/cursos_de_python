"""
36. Leia a altura e o raio de um cilíndro circular e imprima o volume do cilindro. O volume
de um cilíndro circular é calculado por meio da seguinte fórmula: V = pi * raio² * alfura,
onde pi = 3.141542
"""
pi = 3.141542
altura = float(input('Digite a altura do cilindro circular: '))
raio = float(input('Digite o raio do cilindro circular: '))
volume = pi * (raio ** 2) * altura


print(f'O volume é {volume}')
