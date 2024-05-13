#faça um programa que ordene os dias da semana
'''dia = int(input ("Informe um dia da semana: "))
match dia:
    case 1:
        print ("Domingo")
    case 2:
        print ("Segunda")
    case 3:
       print ("Terça") 
    case 4:
        print ("Quarta")
    case 5:
        print ("Quinta")
    case 6:
       print ("Sexta")
    case 7:
        print ("Sábado")
    case _:
        print ("Valor inválido!")'''



#Você está programando o sistema de um hotel. Nele o cliente possui 4 opções: 1. reservar um apartamento, 2. realizar check-in, 3. realizar check-out, 4. chamar serviço de quarto. Escreva mensagens condizentes com a opção selecionada.

'''print ("Bem vindo ao Hotel Adriel! Selecione o serviço desejado:")
print ("1 - Reservar um apartamento")
print ("2 - Realizar check-in")
print ("3 - Realizar check-out")
print ("3 - Chamar seriço de quarto")
opcao = int(input("Digite o número da opção desejada: "))
match opcao:
    case 1:
        print("Reserva realizada com sucesso!")
    case 2:
        print("Check-in realizado com sucesso!")
    case 3:
        print ("Check-out realizado com sucesso!")
    case 4:
        print ("O serviço de quarto já está a caminho")
    case _:
        print ("Opção inválida!")'''



#Faça um programa que peça ao usuário que informe seu sexo, F - Feminino, M - Masculino. "Genêro Masculino", "Genêro Feminino", "Genêro não identificado"

'''sexo = input ("Informe seu sexo (F ou M): ").upper() #.upper() - converte para maiusculo.  .lower() = converte para minisculo
match sexo:
    case "F":
        print ("Genêro Feminino")
    case "M":
        print ("Genêro Masculino")
    case _:
        print ("Genêro não identificado")'''


#Dado o valor de um produto e a forma de pagamento. 1 - à vista, 2 - à prazo. Caso o produto for pago à vista aplique um desconto de 10% antes de mostrar o valor final, senão informe o valor original do produto. 10% de um produto = valor*0.90

'''valorProd = float(input ("Digite o valor do produto: R$"))
print ("OPÇÕES DE PAGAMENTO: ")
print ("1 - à vista")
print ("2 - à prazo")
opcao = int(input ("Escolha a forma de pagamento: "))

match opcao:
    case 1:
        valor = (valorProd*0.90)
        print ("O valor a ser pago é: R$", valor)
    case 2:
        print ("O valor a ser pago é: R$", valorProd)
    case _:
        print ("Não roubarás!")'''


#Faça um programa que peça ao usuário dois valores e o tipo de operação que irá ser realizada. Soma, Subtração, multiplicação, Divisão. Ao final imprima o resultado da operação selecionada.

'''v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))
print ("Operadores:")
print ("1 - Soma")
print ("2 - Subtração")
print ("3 - Multiplicação")
print ("4 - Divisão")
op = int(input("Escolha a operação desejada: "))
match op:
    case 1:
        resultado = v1+v2
        print ("A soma dos dois valores é: ", resultado)
    case 2:
        resultado = v1-v2
        print ("A subtração dos dois valores é: ", resultado)
    case 3:
        resultado = v1*v2
        print ("A multiplicação dos dois valores é: ", resultado)
    case 4:
        resultado = v1/v2
        print ("A divisão dos dois valores é: ", resultado)
    case _:
        print ("Opção inválida")'''


#Faça um programa que calcule o "peso ideal" de um usuário de acordo com um caractere identificador de gênero ("M" para masculino ou "F" para feminino). Insira o gênero e a altura. Peso ideal masculino: (72.7*altura)-58, Peso ideal feminino: (62.1*altura)-44.7

genero = input("Informe seu gênero (F ou M): ").upper()
altura = float(input("Informe sua altura: "))
match genero:
    case "F":
        resultado = (62.1*altura)-44.7
        print ("Seu peso ideal é: ", resultado)
    case "M":
        resultado = (72.7*altura)-58
        print ("Seu peso ideal é: ", resultado)
    case _:
        print ("Opção inválida")
