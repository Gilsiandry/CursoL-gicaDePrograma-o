#Questão 1
'''sexo = input ("Informe seu sexo (F ou M): ").upper()

if sexo == "F":
    altura = float(input ("Informe sua altura em metros (x.xx): "))
    if altura >=1.60:
        print ("Você está apta para se alistar no exécito.")
    else:
        print ("Inápta")

elif sexo == "M":
    altura = float(input ("Informe sua altura em metros (x.xx): "))
    if altura >=1.70:
       print ("Você está apto para se alistar no exécito.")
    else:
        print ("Inápto")
else:
    print ("Valor não esperado.")'''



#Questão 2
'''n1 = float(input ("Informe a primeira nota: "))
n2 = float(input ("Informe a segunda nota: "))
media = (n1+n2)/2
if (media >= 9 and media <=10):
    print ("A")
elif (media >= 7.5) and (media <9):
    print ("B")
elif (media >= 6) and (media <7.5):
    print ("C")
elif (media >= 4) and (media <6):
    print ("D")
elif (media < 4) and (media >=0):
    print ("E")
else:
    ("Opção inválida")'''


#Questão 3
print ("1 - Converter de Celsius para Fahrenheit")
print ("2 - Converter de Fahrenheit para Celsius")

converte = int(input ("Escolha o tipo de converção que deseja fazer (1 ou 2): "))
match converte:
    case 1:
        temperatura = float(input ("Informe a temperatura em Celsius: "))
        Fahrenheit = (temperatura*9/5)+32
        print ("O resultado da temperatuta", temperatura, "em Fahrenheit é: ", Fahrenheit )


    case 2:
        temperatura = float(input ("Informe a temperatura em Fahrenheit: "))
        Celsius = (temperatura-32)*5/9
        print ("O resultado da temperatuta", temperatura, "em Fahrenheit é: ", Celsius )

    case _:
        print ("Opção inválida")
