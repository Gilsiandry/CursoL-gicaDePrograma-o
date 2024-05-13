#cls limpa o proptcomand


lista = ["Abacate", "Banana", "Abacaxi", "Manga", "Açaí", "Buruti", "Murici", "Uva","Maçã"] #para abrir uma lista, basta criar uma variável e colocar os itens entre colchetes e separar os itens por vírgula

lista [0] = "Cupuaçau" #substitui o valor da posição []
print (list [0])

lista.append ("Pêra") # append adiciona ítens à lista
lista.append ("Cajú")

'''for frutas in lista:
    print (frutas)'''

for i in range (0,9,1): #0 inicio da lista, 9 quantidade de vezes que vai rodar e 1 quantas  vezes por vez vai rodar. Se não declarar os valores da extremidade, por padrão sempre iniciará na posição  e veriricar de 1 em 1, logo a especificação é pode ser otimitada se desejar tal funcionamento.
    print (lista [i])


'''seq = [1,2,3,4,5]
for i in seq:
    print (i)'''
