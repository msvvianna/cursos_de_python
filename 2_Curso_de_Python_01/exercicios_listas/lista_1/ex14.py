"""
14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R=Grau *pi/180, sendo G o ângulo em graus e R em radianos e pi = 3.14.

"""
pi = 3.14
angle = float(input('Enter an angle: '))
radian = (angle * pi) / 180
print(f'The result is {radian} radians.')
