'''contador = 0
while contador<10:
    print (contador)
    contador = contador +1     #essa linha também pode ser escrito: contador += 1

#Faça que contador que imprima os número ímpares menores que 1000
contador = 0
while contador<1000:
    print (contador)
    contador +=2

#Faça que contador que imprima os número pares menores que 1000
contador = 1
while contador<1000:
    print (contador)
    contador +=2'''

# Faça um programa que peça uma nota, entre zero e dez, mostre uma mensagem caso o valor seja inválido e continue pendindo até que o usuário informe um valor válido.
'''nota = float(input("Digite uma nota entre 0 e 10: "))
while nota <0 or nota >10:
    print ("Nota inválida. Informe uma nota entre 0 e 10!")
    nota = float(input("Digite uma nota: "))
print ("Nota válida.")'''


#Faça um programa que peça um nome de usuário e senha, não aceite que o usuário digite a senha igual o nome de usuário.
'''usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")
while senha == usuario:
    print ("Senha inválida. Informe uma senha diferente do usuário: ")
    senha = input("Digite uma senha: ")
print ("Senha válida")'''

#Faça um programa que leia e valide as seguintes informações: - Nome: maior que 1 caracter, *len(nome) = retorna o tamanho do nome, idade: 0 ou 150, salário: maior que 0, sexo: F ou M, estado civil: s c v d
'''nome = input("Digite seu nome: ")
while len(nome) <=1:
    print ("Nome inválido.")
    nome = input("Digite seu nome: ")

idade = int(input("Informe sua idade: "))
while idade <0 or idade >150:
    print ("Idade inválido.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Informe seu salário: "))
while salario <0:
    print ("Salário inválido.")
    salario = float(input("Informe seu salário: "))

sexo = input("Informe seu sexo (F ou M): ").upper()
while sexo != "F" and sexo != "M":
    print ("Sexo inválido.")
    sexo = input("Informe seu sexo (F ou M): ")

status = input("Informe seu estado civil: ").upper()
while status != "S" and status != "C" and status != "V" and status != "D":
    print ("Status inválido.")
    status = input("Informe seu estado civil: ")

print ("Todas as informações foram inseridas com sucesso!")'''


#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. EX: 5! = 5*4*3*2*1
num = int(input("Digite um número: "))
fatorial = num
num = num-1
while num >=1:
    fatorial = fatorial*num
    num -=1
print ("Resultado é: ", fatorial)