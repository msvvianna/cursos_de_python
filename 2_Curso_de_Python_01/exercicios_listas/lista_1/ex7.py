"""
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
AA fórmula de conversão é: C = (F — 32.0)*5/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.

"""
temperature_fahrenheit = float(
    input('Enter enter the temperature in degrees Fahrenheit: '))
temperature_celsius = ((temperature_fahrenheit - 32.0) * 5) / 9.0
print(f'The temperature in Celsius is: {temperature_celsius}')
