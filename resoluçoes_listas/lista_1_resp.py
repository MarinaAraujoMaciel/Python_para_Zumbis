# LISTA DE EXERCICIO I --- MARINA ANGELA NOBRE ARAÚJO MACIEL



# 1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números

number1 = int(input('um numero: '))
number2 = int(input('um numero: '))
print (number1 + number2)

# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

metros = int(input ('coloque o numero desejado a ser convertido em mm: '))
mm = metros  *  1000
print (f'{mm:} mm')

# 3) Escreva um programa que leia a quantidade de dias, horas,
# minutos e segundos do usuário. Calcule
# o total em segundos.

d = int (input('Dias: '))
h = int (input('Horas: '))
m = int (input('Minutos: '))
s = int (input('Segundos: '))

total = d * 24 * 60 * 60 + h * 60 * 60 + m *50 + s
print (total)

#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('salario: '))
desconto = int(input('desconto: '))
novo_salario = salario - salario * desconto / 100
print (f'novo salario R$ {novo_salario: .2f}')


# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.

mercadoria = float (input( 'preço: '))
desconto = int(input (' valor do desconto: '))
valor = mercadoria - mercadoria * desconto/100
print (f'R$ {valor: 2.f}')

# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.

d = float( input('distancia km: '))
v = float ( input ('vel. media km/h: '))
t = d / v
print (f'tempo: {t: .1f}')

# 7) Converta uma temperatura digitada em Celsius para Fahrenheit.
""" F = 9*c /5 + 32 """

c = float(input('celsius: '))

f = 9 * c / 5 + 32

print (f'{f: .2f} FAHRENHEIT')

# 8) Faça agora o contrário, de Fahrenheit para Celsius. c = (f-32) * 5/9

f = float(input('Fahrenheit: '))
c = (f-32) * 5/9

print (f'{c: .2f} Celsius')

# 9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('km rodados: '))
dias = int(input('dias rodados: '))

preço= 60 * dias + 0.15 * km
print ( f' R$ {preço: .2f}')


# 10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
# Exiba o total de dias.

cigarros = int( input ('quantos cigarros voce fuma por dia?: '))
anos = int( input ('quantos anos voce já fumou?: '))

cigarros_total = anos * 365 * cigarros
dias = cigarros_total / 144

print(f'voce perdeu {dias: .1f} dias')


# 11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
# a um milhão.

print (len(str(2 ** 1000000)))