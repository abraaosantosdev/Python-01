#007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Nome do aluno: ')
n1 = float(input('Nota da 1ª Unidade: '))
n2 = float(input('Nota da 2ª Unidade: '))
m = (n1 + n2) / 2
print('A média do aluno {} é {:.1f}'.format(nome, m))
