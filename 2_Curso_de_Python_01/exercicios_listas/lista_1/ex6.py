"""
6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
Afórmula de conversão é: F = (C'* 9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.

"""

temperature_celsius = float(
    input('Enter enter the temperature in degrees Celsius: '))
temperature_fahrenheit = (temperature_celsius * 9.0 / 5.0) + 32
print(f'The temperature in Fahrenheit is: {temperature_fahrenheit}')
