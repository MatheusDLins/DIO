set([1, 2, 3, 1, 3, 4]) #{1, 2, 3, 4}

set("abacaxi") # {'b', 'i', 'a', 'x', 'c'}

set(("palio", "gol", "celta", "palio")) #{'celta', 'palio', 'gol'}

#Conjuntos não suportam indexação ou fatiamento, precisa converter para lista

numeros = {1, 2, 3, 2}

numeros = list(numeros)

numeros[0] # 1

#Percorrendo conjuntos

carros = {"gol", "celta", "palio"}

# for carro in carros:
#     print(carro)

#Enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")