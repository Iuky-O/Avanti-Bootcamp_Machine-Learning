#Função para achar elementos unicos das listas
def acha_elementos_unicos(lista_Um, lista_Dois):
    
    lista_elementos_unicos = []
    
    for elemento in lista_Um:
        if elemento not in lista_Dois and elemento not in lista_elementos_unicos:
            lista_elementos_unicos.append(elemento)
            
    for elemento in lista_Dois:
        if elemento not in lista_Um and elemento not in lista_elementos_unicos:
            lista_elementos_unicos.append(elemento)
            
    return lista_elementos_unicos
    
    
#Pede o tamanho das lista
Numeros_list_1 = int(input("Quantos elementos na Lista 1? "))
Numeros_list_2 = int(input("Quantos elementos na Lista 2? "))

lista_Um = []
lista_Dois =[]

aux = 0
aux2 = 0

#preenche a lista de numeros
print("\n Lista 1: \n")

while aux < Numeros_list_1:
    numero = int(input(f"Digite o valor da posição ({aux + 1}): "))
    lista_Um.append(numero)
    
    aux = aux + 1
    
    
print("\n Lista 2: \n")

while aux2 < Numeros_list_2:
    numero = int(input(f"Digite o valor da posição ({aux2 + 1}): "))
    lista_Dois.append(numero)
    
    aux2 = aux2 + 1

#Exibe as listas e os numeros que estão presentes em apenas uma
print(f"Lista 1: {lista_Um}")
print(f"Lista 2: {lista_Dois}")
print(f"Elementos unicos: {acha_elementos_unicos(lista_Um, lista_Dois)}")
