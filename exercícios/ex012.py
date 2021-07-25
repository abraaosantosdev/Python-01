#012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('=' * 31)
p = float(input(' Cupom de 5%, só no pix.\n Qual o valor do produto: R$'))
d = p - (p * 5 / 100)
print('=' * 31)
print('  O cupom de 5% foi aplicado.\n  Valor final: R${:.2f} reais.'.format(d))
print('=' * 31)
