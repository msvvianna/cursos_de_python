"""
21. Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula
de conversão é: K = L+0,45, sendo K a massa em quilogramas e L a massa em libras.
"""

reference_conversion = 2.205
pounds = float(input('Enter an weight in pounds: '))
conversion = pounds / reference_conversion

print(
    f'The conversion result in pounds to kg is: {conversion} kg')
