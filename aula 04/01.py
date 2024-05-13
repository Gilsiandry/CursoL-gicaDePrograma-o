#faça um programa que peça seu nome, sua idade e o curso que você está matriculado. No final imprima a seguinte mensagem: ("Olá, eu me chamo", nome, "tenho" , idade, "anos de idade e estou fazendo o curso de" , curso)
'''nome = input ("Digite seu nome: ")
idade = int(input ("Informe sua idade: "))
curso = input ("Digite o curso que você está matriculado: ")
print ("Olá, eu me chamo", nome, " tenho" , idade, " anos de idade e estou fazendo o curso de" , curso)'''



'''n1 = 0
n2 = 5
media = (n1+n2)/2
if media >= 7: # usa : para terminar a linha do if e do else
    print ("Aprovado")
else:
    if media >= 5:
        print ("Recuperação")
    else: 
        print ("Reprovado")


#para juntar if e else usa elif (estrutura aninhada):

if media >= 7: # usa : para terminar a linha do if e do else
    print ("Aprovado")
elif media >= 5:
        print ("Recuperação")
    else: 
        print ("Reprovado")'''




#Faça um programa que peça os valores de x e y. Se o valor de x for maior que y: escreva: "X é maior que Y"
'''X = int(input ("Informe o valor de X: "))
Y= int(input ("Informe o valor de Y: "))
if X>Y:
    print ("X é maior que Y")
elif X<Y:
    print ("X é menor que Y")
else:
    print ("X é igual a Y")'''



#Faça um programa que peça um valor e mostre na tela se ele é positivo ou negativo
'''valor = int(input ("Digite um número: "))
if (valor>=0):
    print ("O número digitado é positivo")
else:
    print ("O número digitado é negativo")'''



#Faça um programa que verifique se uma letra digitada é "F" ou "M'". conforme a letra, escreva: F- Feminino, M - Masculino, valor não encontrado
'''sexo = input ("Informe seu sexo: ")
if sexo=="F" or sexo=="f":
    print ("Feminino")
elif sexo=="M" or sexo=="m":
    print ("Masculino")
else:
    print("Valor não encontrado")'''



#Faça um programa que leia três números e mostre o maior deles
'''n1 = input ("Digite um número: ")
n2 = input ("Digite outro número: ")
n3 = input ("Digite mais um número: ")
if n1>n2 and n1>n3:
    maior = n1
elif n2>n1 and n2>n3:
    maior = n2
else:
    maior = n3
print (maior, "é o número maior")'''


#Faça um programa que pergunte que turno você estuda. Peça para digitar M - matutino, V - vespertino e N - noturno. Imprima a mensagem "Bom dia", "Boa tarde", "Boa noite" ou "Valor inválido", conforme o caso.
'''turno = input ("Informe o turno que você estuda: ")
if turno=="M" or turno=="m":
    print ("Bom dia")
elif turno=="V" or turno=="v":
    print ("Boa tarde")
elif turno == "N" or turno == "n":
    print ("Boa noite")
else:
    print("Valor inválido")'''


#Faça um programa que faça 5 perguntas para uma pessoa suspeita de um crime. As perguntas são: a "Telefonou para a vítima?", b "Esteve no local do crime", c "Mora perto da vítima". "Devia para a vítima", e "Já trabalhou com a vítima". O programa no final deve classificar a pessoa como suspeita se respondeu positivo para 2 perguntas, cúmplice se respondeu positivo entre 3 e 4, assassino se respondeu todas a 5 positivo.
a=input ("Telefonou para a vítima? ")
b=input ("Esteve no local do crime? ")
c=input ("Mora perto da vítima? ")
d=input ("Devia para a vítima? ")
e=input ("Já trabalhou com a vítima? ")
conte = 0
if a=="sim":
    conte = conte+1
if b=="sim":
    conte +=1
if c=="sim":
    conte +=1
if d=="sim":
    conte +=1
if e=="sim":
    conte +=1

if conte==2:
    print ("Suspeito")
elif conte ==3 or conte ==4:
    print ("Cúmplice")
elif conte ==5:
    print ("Assassino")
else:
    print ("Inocente")