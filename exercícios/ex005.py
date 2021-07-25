#005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um número: '))
ante = num - 1
suce = num + 1
print('O antecessor do número {} é {} e seu sucessor é {}'.format(num, ante, suce))
