"""
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi da 12%
"""

desconto = 12
valor_produto = float(input('Digite o valor do produto: '))
pagamento = valor_produto - (valor_produto * (desconto / 100))

print(f'Valor a pagar com desconto de 12% R$ {pagamento}')
