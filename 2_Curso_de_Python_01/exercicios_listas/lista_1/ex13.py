"""

13. Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
conversão é: M = km/h / miles sendo K a distância em quilômetros e M em milhas.

"""
velocity = float(input('Enter a velocity in km/h: '))
conversion = velocity / 1.61

print(f'The result of converting km/h to miles is: {conversion}')
