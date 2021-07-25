#015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagarm sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

d = int(input('Quantos dias alugado: '))
p = float(input('Qual a quatidade de Km percorridos:'))
v = d * 60 + p * 0.15
print('Você deverá pagar R${:.2f} reais'.format(v))
