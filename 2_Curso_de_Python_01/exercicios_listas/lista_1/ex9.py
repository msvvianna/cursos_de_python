"""
9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.

"""

temperature_celsius = float(
    input('Enter enter the temperature in degrees celsius: '))
temperature_kelvin = temperature_celsius + 273.15
print(f'The temperature in Celsius is: {temperature_kelvin}')
