"""
27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m?.
AA fórmula de conversão é: M = H + 10000, sendo M a área em metros quadrados e H
a área em hectares.

"""
reference_convertion = 1 / 10000
hectares = float(input('Enter an length in hectares: '))
conversion = hectares / reference_convertion

print(
    f'The conversion result in hectares to square meters is: {conversion} square meters.')
