#008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = int(input('Digite o valor para conversão: '))
cent = metro * 100
mili = metro * 1000
print('{} metros convertido para centímetros é {} e em milímetros é {}.'.format(metro, cent, mili))