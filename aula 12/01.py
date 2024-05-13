nomes = ["Gil", "Lig", "Lua", "Sol", "Lia", "Bia"]
numeros = [8,18,28, 38]
frac = [1.8, 2.8, 3.8, 4.8]

nomes.append("Amir") # linha para adicionar uma informação no final da lista no vetor. Informação adicional vai entre ()
nomes.insert (0,"Adriel") # linha para adicionar uma informação em uma posição específica. É preciso indicar a posição e o valor repectivamente)

nomes.remove ("Gil") #apaga informação
removido = nomes.pop(2) #remove e retorna informação em outra variável
print (removido)

vezes = nomes.count ("Sol") #contador, para contar quantas vezes um item se repete
print (vezes)

len(nomes) #retorna o número de elementos de uma lista - tamanho
print (len(nomes))


nomes [2] = "Lua Cheia" # linha para alterar uma informação no vetor. A posição é escolhida especificando o i dentro de []
for i in nomes:
    print (i)