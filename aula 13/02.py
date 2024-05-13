# Faça um programa que preenche uma matrix 3x3, com valores inseridos pelo usuário. no final imprima.
'''matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(3): #para matrix quadrada pode escrever os for's com len(variaveal), para não precisar especificar o número de repetições, ficando assim: for i in range(len(matriz)): &  for j in range(len(matriz)):
    for j in range(3):
        matriz[i][j] = int(input("Digite um valor: "))

for i in range(3):
    for j in range(3):
        print(matriz[i][j])'''

#outra forma de fazer o print
'''matriz = [[0]*3 for k in range(3)] #k é uma variável, poderia ser outra coisa

for i in range(len(matriz)): 
    for j in range(len(matriz)):
        print("Insira o valor na matriz [",i,"][",j,"]: ")
        matriz[i][j] = int(input())

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j])'''


# Faça um programa que leia uma matriz 4x4 (pode criar estático) e conte quantos valores maiores que 10 estão inseridos nessa matriz.
'''A = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
maior10 = 0
for i in range(len(A)):
    for j in range (len(A)):
        if A[i][j] >10:
            maior10 +=1
print ("Na matriz A, existem", maior10, "valores maior que 10")'''


#Declare uma matriz 5x5. Preencha com 1 diagonal principal e com e com 0 os demais elementos. Escreva ao final a matriz obtida.
'''matriz = [[0]*5 for k in range(5)]
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
         matriz[i][j] = 1
print (matriz)'''

# outra forma de fazer
matriz = [[0]*5 for k in range(5)]
for i in range (5):
    matriz [i][i]=1
for i in matriz:
   print (i)