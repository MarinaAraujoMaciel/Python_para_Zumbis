""" Resposta lista de exercicios Python 4 """

import random
'''


sorteio = random.sample(range(100), 10)

maior = sorteio[0]
menor = sorteio[0]

print (sorteio)

for a in sorteio[1: ]:
    if a > maior : maior = a
    if a < maior : menor = a
print (f'Maior: {maior}')
print (f'Menor: {menor}')


'''
numeros = random.sample(range(100), 20)

par = list()
impares = list()

print (f'numeros sortidos: {numeros}')
for a in numeros:
    if a % 2 != 0:
        impares.append(a)
    else:
        par.append(a)
print (f'pares: {par}')

print (f'impares: {impares}')
