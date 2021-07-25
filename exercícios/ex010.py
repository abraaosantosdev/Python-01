#010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Cotação do dolar: R$'))
dol = 5.20
cot = real / dol
print('Cotação: US${:.2f} dólares.'.format(cot))
