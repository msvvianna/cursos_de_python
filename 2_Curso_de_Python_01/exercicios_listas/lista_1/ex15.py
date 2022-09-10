"""

15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180/pi, sendo G o ângulo em graus e R em radianos e pi = 3.14

"""
pi = 3.14
radian = float(input('Enter an radians: '))
angle = (radian * 180) / pi
print(f'The result is {angle} angle.')
