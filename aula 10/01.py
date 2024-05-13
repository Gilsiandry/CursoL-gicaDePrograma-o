#Faça um programa que peça ao usuário que digite sua senha para acessar o sistema. A senha correta é "senha123", caso digite a senha incorreta, peça para inserir a senha novamente.
'''senha = input("Digite uma senha: ")
while senha != "senha123":
    print ("Senha inválida. Tente novamente!")
    senha = input("Digite uma senha: ")
print ("Senha válida")'''


#Faça um programa que leia 5 números e informe a soma e a média dos números
'''soma = 0
for i in range (5):
    num = int(input("Digite um número: "))
    soma = soma+num
media = soma/5
print ("A soma dos números é: " , soma , "e a média é: " , media)'''


#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50
'''for i in range (1,50,2):
    print (i)'''

#Faça um programa que recebe dois números inteiros e gere os números inteiros que estão n intervalo compreendido por eles
'''num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))
for i in range (num1,num2+1,1):
     print (i)'''


#Faça um programa, utilizando for e listas, que peça o nome de três pessoas em uma lista A e três pessoas em uma lista B, mostre na tela três duplas compostas pelas pessoas da lista A e B.
'''listaA = []
listaB = []
for i in range (3):
    listaA.append (input ("Informe um nome : "))
    
for i in range (3):
    listaB.append (input ("Informe um nome : "))

for i in range (3):
    print (listaA[i], "e", listaB [i])'''

# Faça um programa para adivinhar qual o número que o computador "pensou". Usando a função random.randint(1,10), o computador irá escolher um número entre 1  e 10, você irá informar um número até acertar qual número ele escolheu. Obs: necessário informar o módulo Random do python. Usar o comando função random.randint ()
import random
num = random.randint(1,10)
tentativa = int(input("Escolha um número: "))
while tentativa != num:
    if tentativa > num:
        print ("Errou! O número é menor.")
    else:
        print ("Errou! O número é maior.")
    tentativa = int(input("Escolha um número: "))
print ("Acertou!")
