"""
26. Leia um valor de área em metros quadrados e apresente-o convertido em hectares.
.A fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados e H
a área em hectares.

"""

reference_convertion = 1 / 10000
square_meters = float(input('Enter an length in square meters: '))
conversion = square_meters * reference_convertion

print(
    f'The conversion result in square meters to hectares is: {conversion} hectares.')
