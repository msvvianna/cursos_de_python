"""
24. Leia um valor de área em metros quadrados  e apresente-o convertido em acres. A
fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados e À
aárea em acres.
"""

reference_convertion = 0.000247
square_meters = float(input('Enter an length in square meters: '))
conversion = square_meters * reference_convertion

print(
    f'The conversion result in square meters to acres is: {conversion} acres.')
