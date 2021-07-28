#016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

n = float(input('Digite um número: '))
int = trunc(n)
print('O número {} tem a porção inteira {}.'.format(n, int))
