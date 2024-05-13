# Questão 1
'''senha = input("Digite uma senha de quatro dígitos: ")
match senha:
    case "1234":
        print ("Acesso permitido")
    case _:
        print ("Acesso negado")'''


#Questão 2
'''compra = int(input("Digite o número de maçãs que deseja comprar: "))
if (compra <12):
    preço = compra*0.30
    print ("Você comprou", compra, "maças, o valor da sua compra foi de R$", preço)
elif (compra >=12):
    preço = compra*0.25
    print ("Você comprou", compra, "maças, o valor da sua compra foi de R$", preço)
else:
    print("Operação inválida")'''



#Questão 3
'''idade = int(input("Digite sua idade: "))
if idade == 0 or idade <= 12:
    print ("Criança")
elif idade == 13 or idade <= 19:
    print ("Adolescente")
elif idade == 20 or idade <= 59:
    print ("Adulto")
elif idade >= 60:
    print ("Idoso")
else:
    print("Operação inválida")'''


#Questão 4
'''valorcompra = int(input("Digite o valor da compra: "))
print ("Codigo do cliente:")
print ("1 - Cliente comum")
print ("2 - Funcionário")
print ("3 - Cliente vip")
codcliente = int(input("Digite o código do cliente: "))
match codcliente:
    case 1:
        valortotal = valorcompra
        print ("O valor a ser pago é: R$", valortotal)
    case 2:
        valortotal = valorcompra*0.9
        print ("O valor a ser pago é: R$", valortotal)
    case 3:
        valortotal = valorcompra*0.95
        print ("O valor a ser pago é: R$", valortotal)
    case _:
        print ("Opção inválida!")'''



#Questão 5
'''v1 = int(input("Digite um valor inteiro: "))
v2 = int(input("Digite outro valor inteiro: "))
v3 = int(input("Digite mais um valor inteiro: "))
if v1<v2<v3:
    menor = v1
    meio = v2
    maior = v3

elif v2<v1<v3:
    menor = v2
    meio = v1
    maior = v3

elif v3<v1<v2:
    menor = v3
    meio = v1
    maior = v2

elif v2<v3<v1:
    menor = v2
    meio = v3
    maior = v1

else:
   menor = v3
   meio = v2
   maior = v1

print ("A ordem crescente dos número é: ", menor, meio, maior)'''


#Questão 6
'''l1 = int(input("Digite um valor de um lado: "))
l2 = int(input("Digite o valor de outro lado: "))
l3 = int(input("Digite o valor de mais um lado: "))
if l1==l2 and l1==l3 and l2==l3:
    print ("É um triângulo equilátero")
elif l1!=l2 and l1!=l3 and l2!=l3:
    print ("É um triângulo escaleno")
else:
    print ("É um triangulo isóscele")'''


#Questão 7 - Faça um programa que peça um número correspondente a um determinado ano e em seguinda informe se este ano é ou não bissexto. Anos bixssestos são múltiplos de 4, como 1996, 200, 2004 e etc (podem ser divididos por 4 deixando resto 0). Porém há uma exceção: múltiplos de 100 que não sejam múltiplos de 400 (se for múltiplo de 100 automaticamente é de 4)
ano = int(input("Informe um ano: "))
if (ano%400 == 0 and ano%100!=0) or ano%4==0:
    print ("Ano bissexto")
else:
    print ("Ano não bissexto")
