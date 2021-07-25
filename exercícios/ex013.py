#013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual seu salário atual: R$'))
n = s + (s * 15 / 100)
print('', '=' * 44)
print('|| Você será agrecido com 15% de aumento.    ||\n|| Seu novo salário será de R${:.2f} reais. ||'.format(n))
print('', '=' * 44)
