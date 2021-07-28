#018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor e tangente desse ângulo

from math import cos, sin, tan, radians

a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('='*35)
print('O Seno do ângulo {} é {:.2f}'.format(a, s))
print('O Cosseno do ângulo {} é {:.2f}'.format(a, c))
print('A Tangente do ângulo {} é {:.2f}'.format(a, t))