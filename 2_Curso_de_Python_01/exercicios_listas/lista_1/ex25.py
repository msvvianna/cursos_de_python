"""
25. Leia um valor de área em acres e apresente-o convertido em metros quadrados. A
fórmula de conversão é: M = A / 0.000247, sendo M a área em metros quadrados e À a
área em acres.
"""
reference_convertion = 0.000247
acres = float(input('Enter an length in acres: '))
conversion = acres / reference_convertion

print(
    f'The conversion result in acres to square meters is: {conversion} square meters.')
