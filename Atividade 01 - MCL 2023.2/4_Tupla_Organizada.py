#Função para organizar pela primeira letra do nome
def organiza(pessoas):
    
    organiza_pessoa = sorted (pessoas, key = lambda x:x[0])
    
    return organiza_pessoa


quantidade = int(input("Quantas pessoas serão lidas? "))

tupla = ()
pessoas = []

#Preenche a lista de tuplas
for i in range(quantidade):
    
    nome = input("Entre com o nome: ")
    idade = int(input(f"Entre com a idade {nome}: "))

    tupla = tuple([nome, idade]) #preenche tupla
    pessoas.append(tupla) #preenche a lista de tuplas


#Exibe a lista de tuplas e a lista organizada
print(f"\n Lista: {pessoas}")
print(f"\n Lista organizada: {organiza(pessoas)}")
    
