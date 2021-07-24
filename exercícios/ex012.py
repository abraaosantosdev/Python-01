#012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = int(input('Cupom de 5% no pix, qual o valor do produto desejável: '))
desc = prod * 0.95
print('==========================\n Cupom de 5% foi aplicado.\n Valor final: {} reais.\n=========================='.format(desc))