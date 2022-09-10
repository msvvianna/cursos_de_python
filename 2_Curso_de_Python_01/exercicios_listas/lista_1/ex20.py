"""
20. Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é: L = K * 2,205 sendo K a massa em quilogramas e L a massa em libras.
"""

reference_conversion = 2.205
kilos = float(input('Enter an weight in kg: '))
conversion = kilos * reference_conversion

print(
    f'The conversion result in kg to pounds is: {conversion} pounds')
