"""
18. Leia um valor de volume em metros cúbicos m e apresente-o convertido em litros. À
fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos.

"""
volume = float(input('Enter a volume in cubics meter: '))
conversion = volume * 1000

print(
    f'The conversion result in cubics meter to liters is: {conversion} liters')
