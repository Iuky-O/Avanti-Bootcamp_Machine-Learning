import math

Numeros = int(input("Digite a quantidade de elementos: "))


Primos = list(range(2, Numeros))

for i in range(2, int(math.sqrt(Numeros)+1)):

  if i in Primos:

    for j in range(i**2, Numeros, i):

      if j in Primos: Primos.remove(j)

print(f"Numeros primos até {Numeros}:")
print(Primos)
