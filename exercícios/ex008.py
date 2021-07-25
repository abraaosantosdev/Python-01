#008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input('Digite o valor para conversão: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida {}m corresponde a:\nkm: {}\nhm: {}\ndam: {}\ndm: {}\ncm: {}'.format(m, km, hm, dam, dm, cm, mm))
