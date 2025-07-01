lista = []

#Adicionar .append

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

lista  #[1, 'Python', [40, 30, 20]]

#Limpar .clear
lista.clear()
lista # []

#copiar .copy
lista2 = lista.copy()
lista2 # []

#Contar recorrência .count
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") #1
cores.count("azul") #2

#Adicionar outra lista .extend

linguagens = ["python", "js", "c"]

linguagens.extend(["java", "csharp"])
#['python', 'js', 'c', 'java', 'csharp']

#Mostrar index .index
linguagens.index("java") # 3

#Excluir item da lista pelo index ou último elemento .pop
print(linguagens)
linguagens.pop() # csharp
print(linguagens)
linguagens.pop(0)
print(linguagens)

#Excluir especifico .remove
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
linguagens #["python", "js", "java", "csharp"]

#Inverter a lista .reverse
linguagens.reverse()
linguagens #['csharp', 'java', 'js', 'python']

#Ordena a lista .sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() #['c', 'csharp', 'java', 'js', 'python']

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) #['python', 'js', 'java', 'csharp', 'c']


#Ordenar por tamanho da palavra
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) #['c', 'js', 'java', 'python', 'csharp']


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) #['python', 'csharp', 'java', 'js', 'c']

#Outra função para ordenar sorted()
linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key=lambda x: len(x)) #['c', 'js', 'java', 'python', 'csharp']

sorted(linguagens, key=lambda x: len(x), reverse=True) #['python', 'csharp', 'java', 'js', 'c']

#Ver o tamanho da lista .len

len(linguagens) #5

