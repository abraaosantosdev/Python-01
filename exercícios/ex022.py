#022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as minúsculas
# Quantas letras ao ttodo, sem considerar espaços
# Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()
print('='*35)
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Total de letra: {}'.format(len(nome) - nome.count(' ')))
#print('Total de letras do 1º nome: {}'.format(nome.find(' ')))
separa = nome.split()
print('Total de letras do 1º nome: {}'.format(len(separa[0])))
