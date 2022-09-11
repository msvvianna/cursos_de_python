"""
30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente
em dólares.
"""

real = float(input('Digite um valor em real R$ '))
cotacao_dolar = float(input('Digite a cotação do dolar hoje $ '))

resultado = real / cotacao_dolar

print(f'R$ {real} correspondem a {resultado} dolares.')
