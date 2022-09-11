"""
34. Leia o valor do raio de um circulo e calcule e imprima a área do circulo correspondente,
A area do circulo é A = pi * raio² , considere pi = 3.141592.
"""
pi = 3.141592
raio = int(input('Digite o raio do circulo: '))
area = pi * (raio ** raio)

print(f'A area do circulo é {area}')
