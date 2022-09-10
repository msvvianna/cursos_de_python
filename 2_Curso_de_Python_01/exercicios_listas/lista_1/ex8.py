"""
8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. À
fórmula de conversão é: C = K — 273.15, sendo € a temperatura em Celsius e K a
temperatura em Kelvin.


"""

temperature_kelvin = float(
    input('Enter enter the temperature in degrees kelvin: '))
temperature_celsius = temperature_kelvin - 273.15
print(f'The temperature in Celsius is: {temperature_celsius}')
