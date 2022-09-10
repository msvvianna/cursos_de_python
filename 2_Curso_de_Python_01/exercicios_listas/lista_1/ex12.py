"""
12. Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K = 1,61* M, sendo K a distância em quilômetros e M em milhas.

"""

velocity = float(input('Enter a velocity in miles: '))
conversion = velocity * 1.61

print(f'The result of converting miles to km/h is: {conversion}')
