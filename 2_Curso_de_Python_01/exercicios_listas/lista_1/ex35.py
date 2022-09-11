"""
35. Sejam a e b os catelos de um triângulo, onde a hipotenusa é obtida pela equação
hipotenusa = raiz a² + b², Faça um programa que receba os valores de a e b e calcule
o valor da hipolenusa através da equação. Imprima o resultado dessa operação.
"""

cateto_a = float(input('Digite o valor do cateto a do triangulo: '))
cateto_b = float(input('Digite o valor do cateto b do triangulo: '))
hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** (1 / 2)


print(f'A hipotenusa é {hipotenusa}')
