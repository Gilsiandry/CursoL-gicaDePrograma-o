# Atividade avaliativa 2

#Questão 1
'''num = int(input("Digite um número: "))
for i in range (1,11):
    print (num*i)'''


#Questão 2
'''soma = 0
num = int(input("Digite a quantidade de mangás da sua coleção: "))
for i in range (num):
    num = int(input("Digite o valor gasto no mangá: "))
    soma = soma+num
media = soma/num
print ("O total investido em mangás é: " , soma , "e a média é: " , media)'''

#Questão 3
print ("CANDIDATOS:")
print ("2101 - Tião do Gás")
print ("2403 - Shaolin Matador de Porco")
print ("1202 - Zé da Manga")
       
tiaoDoGas = 0
shaolinMatadorDePorco = 0
zeDaManga = 0


eleitores = (int(input ("Informe a quantidade de eleitores : ")))
for i in range (eleitores):
    voto = int(input("Digite o número do candidato que deseja votar: "))
    if 2101 == voto:
        tiaoDoGas +=1
    elif 2403 == voto:
        shaolinMatadorDePorco+=1
    elif 1202== voto:
        zeDaManga+=1
print ("O Candidato Tião do Gás recebeu " , tiaoDoGas )
print ("O Candidato Shaolin Matador de Porco recebeu " , shaolinMatadorDePorco)
print ("O Candidato Zé da Manga recebeu " , zeDaManga)