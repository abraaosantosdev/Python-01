#011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

larg = int(input('Qual a largura da parede: '))
altu = int(input('Qual a altura da parede: '))
metq = larg * altu
tinta = metq / 2
print('Precisará para pintar uma parede de {}m², {} latas de tintas.'.format(metq, tinta))