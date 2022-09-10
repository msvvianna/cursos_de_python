"""
19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos. A
fórmula de conversão é: M = L / 1000, sendo L o volume em litros e M o volume em metros
cúbicos.
"""
volume = float(input('Enter a volume in liters: '))
conversion = volume / 1000

print(
    f'The conversion result in liters to cubics meter is: {conversion} cubics meter')
