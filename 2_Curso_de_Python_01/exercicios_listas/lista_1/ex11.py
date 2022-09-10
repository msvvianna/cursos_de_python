"""

11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
em km/h e M em ms.

"""

velocity = float(input('Enter a velocity in m/s '))
conversion = velocity * 3.6

print(f'The result of converting m/s to km/h is: {conversion}')
