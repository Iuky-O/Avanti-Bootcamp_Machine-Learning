
Numeros = int(input("Digite a quantidade de elementos: "))

lista_Numeros = []
maxMin = []
tupla = ()
aux = 0

#preenche a lista de numeros
while aux < Numeros:
    numero = int(input(f"Digite o valor da posição {aux + 1}: "))
    lista_Numeros.append(numero)
    
    aux = aux + 1
    
#Acha o maximo e minimo usando:
tupla = tuple([(max(lista_Numeros)), (min(lista_Numeros))])
maxMin.append(tupla)
    
#Exibe a lista e o segundo maior valor
print(f"Lista: {lista_Numeros}")
print(f"Maior e Menor elementos da lista são respectivamente: {maxMin}")



'''
    Foi criado uma lista de tuplas para preencher a lista com as duas posições 
    para Maximo e para Minimo.
    Assim foi percorrido só uma vez, preenchedo a lista maxMin
    
'''
