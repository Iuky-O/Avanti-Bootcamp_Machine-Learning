import math

#Função para achar numeros primos
def acha_primos(Primos, Numeros):
    for i in range(2, int(math.sqrt(Numeros)+1)):
    
      if i in Primos:
    
        for j in range(i**2, Numeros, i):
    
          if j in Primos: Primos.remove(j)
          
    return Primos
    
    
Numeros = int(input("Digite a quantidade de elementos que vão até < que : "))


Primos = list(range(2, Numeros))

def acha_primos(Primos, Numeros):
    for i in range(2, int(math.sqrt(Numeros)+1)):
    
      if i in Primos:
    
        for j in range(i**2, Numeros, i):
    
          if j in Primos: Primos.remove(j)
          
    return Primos

print(f"Numeros primos < {Numeros}:")
print(acha_primos(Primos, Numeros))
