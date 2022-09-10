"""
23. Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula
de conversão é: J = M / 0.914, sendo J o comprimento em jardas e M o comprimento em
metros.
"""
reference_convertion = 0.914
meters = float(input('Enter an length in meters: '))
conversion = meters / reference_convertion

print(
    f'The conversion result in meters to yards is: {conversion} yards.')
