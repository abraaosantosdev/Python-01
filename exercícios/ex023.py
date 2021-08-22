#023 - Faça um programa que leia um número e mostre na tela cada um dos dígitos separados (unidade, dezenas, centenas, milhar)

num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {} tem'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('milhar: {}'.format(m))

