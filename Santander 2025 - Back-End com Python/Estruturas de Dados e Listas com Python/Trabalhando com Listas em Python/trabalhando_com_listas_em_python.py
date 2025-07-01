frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")
#['p', 'y', 't', 'h', 'o', 'n']

numeros = list(range(10))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
carro[0] #Ferrari
carro[-1] #True

#LISTAS ANINHADAS

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 7, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

#FATIAMENTO
#lista[inicio:fim(não incluso):pulando]
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] #["t", "h", "o", "n"]
lista[:2] #["p", "y"]
lista[1:3] #["y", "t"]
lista[0:3:2] #["p", "t"]
lista[::] #["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

#ITERAR LISTAS

carros = ["gol", "celta", "palio"]

# for carro in carros:
#     print(carro)

#ENUMERATE (ACHAR ÍNDICE)

# for indice, carro in enumerate(carros):
#     print(f"{indice}: {carro}")

# print(carros.index("gol"))

#COMPREENSÃO DE LISTAS

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)

pares = [numero for numero in numeros if numero % 2 == 0]

quadrado = [numero ** 2 for numero in numeros]