"""
53. Faça um programa para ler as dimensões de um terreno (comprimento c e largura l)
bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno
com tela.
"""

comprimento = int(input('Digite o comprimento do terreno: '))
largura = int(input('Digite a largura do terreno: '))
preco_metro_tela = float(input('Digite o valor por metro de tela: '))

custo_final = (comprimento * largura) * preco_metro_tela

print(f'O custo para cercar o terreno é de R$ {custo_final}')
