#ordem da matriz linha [i] - coluna [j], é preciso estar entre dois colchetes e ter vírgula entre as linhas

#exemplo A
'''A = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

for i in range (3):
        for j in range (4):
            print (A[i][j])'''


#Matriz 3x3
'''B = [[1,2,3],
     [4,5,6],
     [7,8,9]]
for i in range (3):
        for j in range (3):
            print (B[i][j])'''


#testes
C = [[1,2,3],
     [4,5,6],
     [7,8,9]]

C[1][1] = 15 #subistitui o valor na matriz

print (C[1][1])
