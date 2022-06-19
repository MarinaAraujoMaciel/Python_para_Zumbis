
""" Lista de Exercícios II --- MNARINA ANGELA NOBRE ARAÚJO MACIEL

1. Faça um Programa que peça os três lados de um triângulo. O programa 
deverá informar se os valores podem ser um triângulo. Indique, caso os 
lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. """


a = int (input ('lado a: '))
b = int (input ('lado b: '))
c = int (input ('lado c: '))

if a < b + c and b < a + c and c < a + b :
    if a == b == c : #a  == b and b == c and  a == c
        print ( 'Equilatero')
    elif  a == b or b == c or a == c:
        print ( 'Isosceles' )
    else:
        print ( 'Escaleno' )
else:
    print ('Não é triangulo' )


""" 2. Determine se um ano é bissexto. Verifique no Google como fazer isso... """

from calendar import isleap

ano = int (input ( 'Insira ano: '))

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')


""" 3. João Papo - de - Pescador, homem de bem, comprou um microcomputador para 
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso 
de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) 
e verifique se há excesso. Se houver, gravar na variável excesso e na variável 
multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
variáveis com o conteúdo ZERO """

peso = float ( input ( ' insira o peso: '))

if peso <= 50 :
    print ('Não exedido, multa zero')
else:
     print ('Multado')
     multa = (peso - 50) * 4
     print (f'R$ {multa: .2f}')


""" 4. Faça um Programa que leia três números e mostre o maior deles. """

a = int(input ('a: '))
b = int(input ('b: '))
c = int(input ('c: '))

maior = a

if ( b > maior) :
    maior = b
elif ( c > maior ) :
    maior = c
print ('Maior: ' , maior)



""" 5. Faça um Programa que leia três números e mostre o maior e o menor deles. """

a = int(input ('a: '))
b = int(input ('b: '))
c = int(input ('c: '))

maior = a

if b > maior :
    maior = b
if c > maior :
    maior = c
print ('Maior: ' , maior)


menor = a

if b > maior :
    maior = b
if c > maior :
    maior = c
print ('menor: ' , menor)



""" 6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS 
e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto 
pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b.-IR (11%) : R$
c.- INSS (8%) : R$
d.-Sindicato ( 5%) : R$
e.= Salário Liquido : R$ """

ganha = int(input ('valor por hora: ' ))
horas = int(input ('horas trabalhadas no mês: '))

bruto = ganha * horas
IR = bruto * 11 / 100
INSS = bruto *  8 / 100
Sindicato = bruto * 5 / 100
Salario = bruto - IR - INSS - Sindicato

print (f'+Salario Bruto   : R$ {bruto: .2f}')
print (f'-IR(11%)         : R$ {IR: .2f}')
print (f'-INSS(8%)        : R$ {INSS: .2f}')
print (f'-Sindicato(5%)   : R$ {Sindicato: .2f}')
print (f'=Salario Liquido : R$ {Salario: .2f}')


""" 7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total. Obs. : somente são vendidos um número inteiro de latas. """

m = int (input('Metros: '))
if m % 54 == 0:
    latas = m / 54
else:
    latas = int (m / 54) + 1
print (f'Vai precisar de {latas} lata(s)')
print (f' R$ {latas * 80: .2f}')