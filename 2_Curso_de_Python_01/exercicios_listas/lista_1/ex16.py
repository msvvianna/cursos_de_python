"""
16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.

"""

inches = 2.54
length_inches = float(input('Enter a length in inches: '))
convertion = length_inches * inches
print(
    f'The conversion result of inches to centimeter is {convertion} centimeters.')
