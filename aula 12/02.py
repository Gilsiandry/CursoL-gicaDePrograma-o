#Faça um programa que peça o nome de um usuário e retorne a quantidade de letras no seu nome.
'''nome = input("Digite seu nome: ")
len(nome)
print (len(nome))'''


# Faça um programa que leia um nome, e diga quantas consoantes foram lidas.
'''nome = input("Digite seu nome: ")
consoante = 0
for i in nome:
    if i != "a" and  i != "e" and i != "i" and i != "o" and i != "u":
        consoante = consoante+1
print (consoante)'''


#Faça um programa que leia 20 números inteiros e armazene em um vetor. Armazene os números pares no vetor PAR e os números ímpares no vetor Impar. Imprima os dois vetores.
'''numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
impar = []
par = []
for i in numeros:
    if i %2 == 0:
        par.append(i)
    else:
        impar.append (i)
print ("Os numeros pares são: ", par)
print ("Os numeros impares são: ", impar)'''


#Faça um programa que possua um vetor chamado A que armazena 6 valores inteiros.
A = [1,0,5,-2,-5,7]
soma = A [0] + A [1] + A [5]
A [4] = 100
for i in A:
    print (i)






