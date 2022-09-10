"""
10. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: 1M = K/3.6, sendo K a velocidade em
km/h e M em m/s.

"""

velocity = float(input('Enter a velocity in km/h: '))
conversion = velocity / 3.6

print(f'The result of converting km/h to m/s is: {conversion}')
