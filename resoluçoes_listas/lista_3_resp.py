""" Resposta lista de exercicios Python 3 """


nota= float(input('digite uma nota:'))
while nota < 0 or nota > 10:
    print('nota entre 0 e 10')
    nota = float(input('digita outra nota:'))


usuário = input('insira um nome para o usuário:')
senha = input('insira uma senha:')
while usuário == senha:
  print('a senha necessita ser diferente do nome do seu usuário')
  usuário = input('usuário: ')
  senha = input('nova senha: ')


população1 = 80000
população2 = 200000
ano = 0
while população1 <= população2:
    população1 = população1 + (população1 * 0.03)
    população2 = população2 + (população2 * 0.015)
    ano = ano + 1
print(ano)


num = int(input('Digite o valor do número: '))
a, b = 1, 1
k = 1 + 1
while k <= num - 2:
    a, b = b, a + b
    k = k + 1
print (b)

a = int(input('insira o valor de a:'))
b = int(input('insira o valor de b:'))
while a % b != 0:
    a, b = b, a%b
print (f'mdc = {b}')

