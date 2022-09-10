"""
22. Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = J * 0.914, sendo J o comprimento em jardas e M o comprimento
em metros.
"""

reference_convertion = 0.914
yards = float(input('Enter an length in yards: '))
conversion = yards * reference_convertion

print(
    f'The conversion result in yards to meters is: {conversion} meters.')
