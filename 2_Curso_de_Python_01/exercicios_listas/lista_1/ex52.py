"""
52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
porcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido.
"""

apostador_1 = float(input('Apostador 1, Digite o valor de contribuição: '))
apostador_2 = float(input('Apostador 2, Digite o valor de contribuição: '))
apostador_3 = float(input('Apostador 3 ,Digite o valor de contribuição: '))

premio = float(input('Digite o valor do premio R$ '))

print(f'O apostador 1 receberá R$ {apostador_1 / 100 * premio}')
print(f'O apostador 2 receberá R$ {apostador_2 / 100 * premio}')
print(f'O apostador 3 receberá R$ {apostador_3 / 100 * premio}')
