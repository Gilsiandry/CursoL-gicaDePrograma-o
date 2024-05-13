#matriz tridimencional = 3x3x3
A = [[[1,2,3],[4,5,6],[7,8,9]],
    [[10,11,12],[13,14,15],[16,17,18]],
    [[19,20,21],[22,23,24],[25,26,27]]]

for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
                print (A[i][j][k])


#outra forma de imprimir
A = [[[1,2,3],[4,5,6],[7,8,9]],
    [[10,11,12],[13,14,15],[16,17,18]],
    [[19,20,21],[22,23,24],[25,26,27]]]

for linha in A:
    for coluna in linha:
        for profundidade in coluna:
            print(profundidade, end=" ")
        print ()
    print ()