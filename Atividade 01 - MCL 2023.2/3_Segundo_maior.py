#Função - verifica se é segundo maior
def achar_segundo_maior(lista_Numeros, Numeros):
    
    maior = 0
    segundo_maior = 0
    aux2 = 0
    
    while aux2 < Numeros:
            
        if lista_Numeros[aux2] > maior:
            
            segundo_maior = maior
            maior = lista_Numeros[aux2]
            
        elif maior > lista_Numeros[aux2] > segundo_maior:
            
            segundo_maior = lista_Numeros[aux2]
                
        aux2 = aux2 + 1
        
    return segundo_maior


Numeros = int(input("Digite a quantidade de elementos: "))

lista_Numeros = []
aux = 0

#preenche a lista de numeros
while aux < Numeros:
    numero = int(input(f"Digite o valor da posição {aux + 1}: "))
    lista_Numeros.append(numero)
    
    aux = aux + 1
    
#Exibe a lista e o segundo maior valor
print(lista_Numeros)
print(f"O segundo maior número: {achar_segundo_maior(lista_Numeros, Numeros)}")

