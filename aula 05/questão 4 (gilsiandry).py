#Aluna: Gilsiandry P. Carvalho

print("INFORME O CONECTIVO QUE DESEJA UTILIZAR!")
print("a = e, b = ou, c = se...então, d = se somente se")
conectivo = input("Escolha uma das opções (a, b, c ou d): ")
p = input("Digite um valor para P: ").upper()
q = input("Digite um valor para q: ").upper()
match conectivo: 
    case "a":
        if p == "V" and q == "V":
            print("P^Q = V")
        elif p == "V" and q == "F":
            print("p^q = F")
        elif p == "F" and q == "V":
            print("p^q = F")
        elif p == "F" and q == "F":
            print("p^q = F")
    case "b": 
        if p == "V" and q == "V":
            print("p v q = V")
        elif p == "V" and q == "F":
            print("p v q = V")
        elif p == "F" and q == "V":
            print(" p v q = V")
        elif p == "F" and q == "F":
            print("p v q = F")
    case "c" :
        if p == "V" and q == "V":
            print("p -> q = V")
        elif p == "V" and "F":
            print("p -> q = F")
        elif p == "F" and q == "V":
            print("p -> q = V")
        elif p == "F" and q == "F":
            print(" p -> q = V")
    case "d" : 
        if p == "V" and q == "V":
            print("p <-> q = V")
        elif p == "V" and q == "F":
            print("p <-> q = F")
        elif p == "F" and q == "V":
            print("p <-> q = F")
        elif p == "F" and q == "F":
            print("p <-> q = V")
    case _:
        ("Opção inválida.")