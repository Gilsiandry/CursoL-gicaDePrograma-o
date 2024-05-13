#Faça um programa que imprima na tela os números de 1 a 20.

'''for i in range (1,21,1): #se começar a contagem da posição 1 é preciso aumentar mais 1 ao valor do número final
    print (i)

    #or

for i in range (0,20,1):
        print (i)

for i in range (2001):
    print (i)

for i in range (1,2001,2):
    print (i)'''

#Faça um programa que leia 5 números, e imprima o maior deles

'''lista = []
maior = 0
for i in range (5):
    lista.append (int(input ("Informe um número: ")))
    if  lista [i] > maior:
        maior = lista[i]
  
print ( "O maior número digitado foi: ", maior)'''




'''A = [1,2,3,4,5]
for i in A: #nessa situação o python sabe onde começa e onde para. Aqui percorre os elementos/indices então imprime os valores de A
    print (i)'''



A = [1,2,3,4,5]
for i in range (5): #no range o programador determina onde começa, onde para, e o passo (1,5,1). Aqui o range percorre a posição então pode imprimir tanto o valor quanto a posição, caso queira
    print (A[i]) #imprime valor


    print ([i])#imprime posição