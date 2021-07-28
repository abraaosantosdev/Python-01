# Importação do todo
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Importação individual
from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

import emoji
print(emoji.emojize('Python is :thumbs_up:'))


